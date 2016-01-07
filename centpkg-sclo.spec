Name:		centpkg-sclo
Version:	0.1
Release:	1%{?dist}
Summary:	Wrapper script around centpkg and cbs utility

Group:		Development/Tools
License:	MIT
URL:		https://github.com/sclorg/centpkg-sclo
Source0:	centpkg-sclo
Source1:	README.md
Source2:	LICENSE
BuildArch:	noarch

Requires:	centos-packager rhpkg

%description
This is a wrapper script around centpkg and cbs utility, that is especially
designed for working with packages and repos in SCLo SIG group.

%prep
%setup -cT
cp %{SOURCE0} %{SOURCE1} %{SOURCE2} .

%build

%install
mkdir -p %{buildroot}%{_bindir}
cp centpkg-sclo %{buildroot}%{_bindir}/${name}

%files
%doc README.md LICENSE
%{_bindir}/%{name}

%changelog
* Thu Jan  7 2016 Honza Horak <hhorak@redhat.com> - 0.1-1
- Initial packaging

