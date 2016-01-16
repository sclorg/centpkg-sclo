# centpkg-sclo

Wrapper script around centpkg and cbs utility, that is especially designed for working with packages and repos in SCLo SIG group.

Currently, since there is no dist-git and look-aside cache working in CentOS for SIG groups, this tool uses repositories on Github space at [https://github.com/sclorg-distgit](https://github.com/sclorg-distgit) and look-aside cache from Fedora. As the build system, CentOS Build System (CBS, at [cbs.centos.org](http://cbs.centos.org) us used.

## Install instructions

This tool is build as RPM in Copr at (https://copr.fedoraproject.org/coprs/hhorak/centpkg-sclo/)[https://copr.fedoraproject.org/coprs/hhorak/centpkg-sclo/].

### Install instructions for Fedora 23
```
sudo dnf copr enable hhorak/centpkg-sclo
sudo dnf copr enable bstinson/centos-packager
sudo yum install centpkg-sclo
```

Or alternatively, if you don't use `dnf copr` plugin:

```
sudo curl https://copr.fedoraproject.org/coprs/hhorak/centpkg-sclo/repo/fedora-23/hhorak-centpkg-sclo-fedora-23.repo >/etc/yum.repos.d/centos-sclo.repo
sudo curl https://copr.fedoraproject.org/coprs/bstinson/centos-packager/repo/fedora-23/bstinson-centos-packager-fedora-23.repo >/etc/yum.repos.d/centos-packager.repo
sudo yum install centpkg-sclo
```

### Install instructions for EPEL 7
```
sudo curl https://copr.fedoraproject.org/coprs/hhorak/centpkg-sclo/repo/epel-7/hhorak-centpkg-sclo-epel-7.repo >/etc/yum.repos.d/centos-sclo.repo
sudo curl https://copr.fedoraproject.org/coprs/bstinson/centos-packager/repo/epel-7/bstinson-centos-packager-epel-7.repo >/etc/yum.repos.d/centos-packager.repo
sudo yum install centpkg-sclo
```

## Usage instructions

API of `centpkg-sclo` was deliberately designed to be the same as we know it from `fedpkg` or what will eventually be in `centpkg`.

That said, all actions, except 'create-branch', work the same as we know it from 'fedpkg'.

Action 'create-branch' creates a new branch in current repository. For creating entirely new repository, go to https://github.com/sclorg-distgit.

### Example of whole workflow when building a new package
```
# 1. Create a repository in GUI at [https://github.com/sclorg-distgit](https://github.com/sclorg-distgit), e.g. mariadb

# 2. Clone the repository locally and enther the directory
$> centpkg-sclo clone mariadb
$> cd mariadb

# 3. Create a new branch according the scheme documented in [https://wiki.centos.org/BrianStinson/GitBranchesandKojiTags](https://wiki.centos.org/BrianStinson/GitBranchesandKojiTags)
$> centpkg-sclo create-branch sig-sclo7-rh-mariadb101-rh

# 4. Import the srpm package
$> centpkg-sclo import rh-mariadb101-mariadb-10.1.10-1.el7.src.rpm

# 5. Commit the changes
$> git commit -am "Initial commit"

# 6. Push the changes
$> git push

# 7. (optionally) Build package locally
$> centpkg-sclo local

# 8. (optionally) Build testing package in CBS
$> centpkd-sclo scratch-build

# 9. (optionally) Create SRPM that may be submitted to CBS manually using `cbs` utility
$> centpkg-sclo srpm

# 10. Finally, build regular package in CBS
$> centpkg-sclo build
```

For questions, suggestions or generally help with building packages in SCLo SIG in CentOS, contact `sclorg@redhat.com` mailing list.
