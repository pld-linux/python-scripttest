#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	scripttest
Summary:	Helper to test command-line scripts
Summary(pl.UTF-8):	Moduł pomocniczy do testowania skryptów linii poleceń
Name:		python-%{module}
Version:	1.3
Release:	10
License:	MIT
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/s/scripttest/%{module}-%{version}.tar.gz
# Source0-md5:	1d1c5117ccfc7b5961cae6c1020c0848
URL:		https://pypi.org/project/scripttest/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
scripttest is a library to help you test your interactive command-line
applications.

With it you can easily run the command (in a subprocess) and see the
output (stdout, stderr) and any file modifications.

%description -l pl.UTF-8
scripttest to biblioteka pomagająca testować interaktywne aplikacje
linii poleceń.

Przy jej użyciu mozna łatwo uruchamiać polecenia (w podprocesie) i
sprawdzać wyjście (stdout, stderr) oraz zmiany dowolnych plików.

%package -n python3-%{module}
Summary:	Helper to test command-line scripts
Summary(pl.UTF-8):	Moduł pomocniczy do testowania skryptów linii poleceń
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-%{module}
scripttest is a library to help you test your interactive command-line
applications.

With it you can easily run the command (in a subprocess) and see the
output (stdout, stderr) and any file modifications.

%description -n python3-%{module} -l pl.UTF-8
scripttest to biblioteka pomagająca testować interaktywne aplikacje
linii poleceń.

Przy jej użyciu mozna łatwo uruchamiać polecenia (w podprocesie) i
sprawdzać wyjście (stdout, stderr) oraz zmiany dowolnych plików.

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

%py_postclean
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
%{py_sitescriptdir}/scripttest.py[co]
%{py_sitescriptdir}/scripttest-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/scripttest.py
%{py3_sitescriptdir}/__pycache__/scripttest.cpython-*.py[co]
%{py3_sitescriptdir}/scripttest-%{version}-py*.egg-info
%endif
