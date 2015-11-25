#
# Conditional build:
%bcond_with	tests	# do perform tests (not included)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	scripttest
Summary:	Helper to test command-line scripts
Name:		python-%{module}
Version:	1.3
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/s/scripttest/%{module}-%{version}.tar.gz
# Source0-md5:	1d1c5117ccfc7b5961cae6c1020c0848
URL:		http://pythonpaste.org/scripttest/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python-pytest
%endif
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
scripttest is a library to help you test your interactive command-line
applications.

With it you can easily run the command (in a subprocess) and see the
output (stdout, stderr) and any file modifications.

%package -n python3-%{module}
Summary:	Helper to test command-line scripts
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
scripttest is a library to help you test your interactive command-line
applications.

With it you can easily run the command (in a subprocess) and see the
output (stdout, stderr) and any file modifications.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/%{module}*.py
%{py_sitescriptdir}/%{module}*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/%{module}.py
%{py3_sitescriptdir}/__pycache__/%{module}.*
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
