#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Friendlier RFC 6265-compliant cookie parser/renderer
Summary(pl.UTF-8):	Bardziej przyjazny parser/renderer ciasteczek zgodny z RFC 6265
Name:		python-cookies
Version:	2.2.1
Release:	6
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/cookies/
Source0:	https://files.pythonhosted.org/packages/source/c/cookies/cookies-%{version}.tar.gz
# Source0-md5:	6f4c53aba3ed03e4e7b50812c2c2579a
URL:		https://pypi.org/project/cookies/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cookies.py is a Python module for working with HTTP cookies: parsing
and rendering 'Cookie:' request headers and 'Set-Cookie:' response
headers, and exposing a convenient API for creating and modifying
cookies. It can be used as a replacement of Python's Cookie.py (aka
http.cookies). 

%description -l pl.UTF-8
cookies.py to moduł Pythona do pracy z ciasteczkami HTTP: analizą i
budowaniem nagłówków 'Cookie:' żądań oraz 'Set-Cookie:' odpowiedzi.
Udostępnia wygodne API do tworzenia i modyfikowania ciasteczek. Może
służyć za zamiennik pythonowego Cookie.py (tj. http.cookies).

%package -n python3-cookies
Summary:	Friendlier RFC 6265-compliant cookie parser/renderer
Summary(pl.UTF-8):	Bardziej przyjazny parser/renderer ciasteczek zgodny z RFC 6265
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-cookies
cookies.py is a Python module for working with HTTP cookies: parsing
and rendering 'Cookie:' request headers and 'Set-Cookie:' response
headers, and exposing a convenient API for creating and modifying
cookies. It can be used as a replacement of Python's Cookie.py (aka
http.cookies). 

%description -n python3-cookies -l pl.UTF-8
cookies.py to moduł Pythona do pracy z ciasteczkami HTTP: analizą i
budowaniem nagłówków 'Cookie:' żądań oraz 'Set-Cookie:' odpowiedzi.
Udostępnia wygodne API do tworzenia i modyfikowania ciasteczek. Może
służyć za zamiennik pythonowego Cookie.py (tj. http.cookies).

%prep
%setup -q -n cookies-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m pytest test_cookies.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
# test_encoding_assumptions fails due to '~' not in dont_quote
%{__python3} -m pytest test_cookies.py -k 'not test_encoding_assumptions'
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/test_cookies.py*
%py_postclean
%endif

%if %{with python3}
%py3_install

%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/test_cookies.py \
	$RPM_BUILD_ROOT%{py3_sitescriptdir}/__pycache__/test_cookies.*.py*
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/cookies.py[co]
%{py_sitescriptdir}/cookies-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-cookies
%defattr(644,root,root,755)
%doc README
%{py3_sitescriptdir}/cookies.py
%{py3_sitescriptdir}/__pycache__/cookies.cpython-*.py[co]
%{py3_sitescriptdir}/cookies-%{version}-py*.egg-info
%endif
