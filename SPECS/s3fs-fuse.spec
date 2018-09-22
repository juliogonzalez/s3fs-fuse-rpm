%global _hardened_build 1
%global _release_simple 2

Name:           s3fs-fuse
Version:        1.84

Release:        %{_release_simple}%{?dist}
Summary:        FUSE-based file system backed by Amazon S3

License:        GPLv2
URL:            https://github.com/s3fs-fuse/s3fs-fuse
Source0:        https://github.com/s3fs-fuse/s3fs-fuse/archive/v%{version}.tar.gz
Source1:        https://github.com/juliogonzalez/s3fs-fuse-rpm/blob/%{version}-%{_release_simple}/SOURCES/passwd-s3fs

Requires:	fuse >= 2.8.4
Requires:       fuse-libs >= 2.8.4
Requires:	curl >= 7.0
Requires:	libxml2 >= 2.6
Requires:	openssl >= 0.9

BuildRequires:  curl-devel, fuse-devel, libxml2-devel, openssl-devel
BuildRequires:	automake, gcc-c++, make
Conflicts:      fuse-s3fs
Obsoletes:	s3fs

%description
s3fs is a FUSE file system that allows you to mount an Amazon S3 bucket as a
local file system. It stores files natively and transparently in S3 (i.e.,
you can use other programs to access the same files). Maximum file size=64GB
(limited by s3fs, not Amazon).
.
s3fs is stable and is being used in number of production environments, e.g.,
rsync backup to s3.

%global debug_package %{nil}

%prep
%setup -q


%build
./autogen.sh
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
cp -p %{SOURCE1} passwd-s3fs


%files
%{_bindir}/s3fs
%{_mandir}/man1/s3fs.1*
%doc AUTHORS README.md ChangeLog COPYING passwd-s3fs


%changelog
* Sat Sep 22 2018 Julio Gonzalez Gil <git@juliogonzalez.es> - 1.84-2
- Build with PIE enabled, as it is required by Fedora
- Remove Group tag, as required by Fedora
- Remove unneeded build requirement for mailcap
- Fix URLs for s3fs-fuse sources

* Sun Jul  8 2018 Julio Gonzalez Gil <git@juliogonzalez.es> - 1.84-1
- Initial build of 1.84 from https://github.com/s3fs-fuse/s3fs-fuse

* Fri Jan  5 2018 William Anderson <william.anderson@indicia.com> - 1.83-1
- Initial build of 1.83 from https://github.com/s3fs-fuse/s3fs-fuse

* Tue May 16 2017 Julio Gonzalez Gil <git@juliogonzalez.es> - 1.82-1
- Initial build of 1.82 from https://github.com/s3fs-fuse/s3fs-fuse

* Tue May 16 2017 Julio Gonzalez Gil <git@juliogonzalez.es> - 1.81-1
- Initial build of 1.81 from https://github.com/s3fs-fuse/s3fs-fuse

* Thu Jul 30 2015 Julio Gonzalez Gil <git@juliogonzalez.es> - 1.80-1
- Initial build of 1.80 from https://github.com/s3fs-fuse/s3fs-fuse

* Thu Jul 30 2015 Julio Gonzalez Gil <git@juliogonzalez.es> - 1.79-1
- Initial build of 1.79 from https://github.com/s3fs-fuse/s3fs-fuse

* Sat Apr 25 2015 Julio Gonzalez Gil <git@juliogonzalez.es> - 1.78-1
- Initial build of 1.78 from https://github.com/s3fs-fuse/s3fs-fuse

* Mon Apr 28 2014 Julio Gonzalez Gil <git@juliogonzalez.es> - 1.77-1
- Initial build of 1.77 from https://github.com/s3fs-fuse/s3fs-fuse

* Thu May 31 2012 Corey Gilmore	<git@cfgci.com> - 1.61-1
- Initial build of 1.61. Disabled generation of useless debug package. Using spec from https://bugzilla.redhat.com/show_bug.cgi?id=725292

* Mon Aug 15 2011 Jorge A Gallegos <kad@blegh.net> - 1.58-5
- Minor mod to get rid of macro in changelog

* Sun Jul 31 2011 Jorge A Gallegos <kad@blegh.net> - 1.58-4
- Got rid of unnecessary buildroot cleaning

* Sun Jul 31 2011 Jorge A Gallegos <kad@blegh.net> - 1.58-3
- Moved passwd-s3fs to docs folder

* Wed Jul 27 2011 Jorge A Gallegos <kad@blegh.net> - 1.58-2
- Added docs to files section in spec
- Password file passwd-s3fs is installed as 0644 and changed in post

* Sun Jul 24 2011 Jorge A Gallegos <kad@blegh.net> - 1.58-1
- Initial build
