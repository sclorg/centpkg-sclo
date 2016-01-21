Name:		centpkg-sclo
Version:	0.1
Release:	8%{?dist}
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
* Thu Jan 21 2016 Honza Horak <hhorak@redhat.com> - 0.1-8
- Count with srpm output to be longer than one line

* Thu Jan 21 2016 Honza Horak <hhorak@redhat.com> - 0.1-7
- Check pkg in tag before building
  Add import command

* Sat Jan 16 2016 Honza Horak <hhorak@redhat.com> - 0.1-6
- Define explicit dist tag for local action

* Sat Jan 16 2016 Honza Horak <hhorak@redhat.com> - 0.1-5
- Run cbs command instead of print it only

* Sat Jan 16 2016 Honza Horak <hhorak@redhat.com> - 0.1-4
- Write better help in README.md and mention help command

* Sat Jan 16 2016 Honza Horak <hhorak@redhat.com> - 0.1-3
- Add new action create-branch
  Use fedpkg instead of rhpkg
  Add better help and error messages

* Thu Jan 07 2016 Honza Horak <hhorak@redhat.com> - 0.1-2
- Do not use centpkg, which is not yet ready

* Thu Jan  7 2016 Honza Horak <hhorak@redhat.com> - 0.1-1
- Initial packaging

