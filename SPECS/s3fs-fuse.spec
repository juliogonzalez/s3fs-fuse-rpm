%global _hardened_build 1
%{!?make_build: %global make_build %{__make} %{?_smp_mflags}}

Name:           s3fs-fuse
Version:        1.95

Release:        1%{?dist}
Summary:        FUSE-based file system backed by Amazon S3

License:        GPL-2.0-or-later
URL:            https://github.com/s3fs-fuse/s3fs-fuse
Source0:        https://github.com/s3fs-fuse/s3fs-fuse/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        passwd-s3fs

Requires:       fuse-libs >= 2.8.4
# Fuse is required to be able to use mount command, /etc/fstab or mount via systemd
Requires:       fuse >= 2.8.4
# To identify the mime-types
Requires:       mailcap
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fuse) >= 2.8.4
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl)
# fuse-s3fs has a binary s3fs too
Conflicts:      fuse-s3fs

%description
s3fs is a FUSE file system that allows you to mount an Amazon S3 bucket as a
local file system. It stores files natively and transparently in S3 (i.e.,
you can use other programs to access the same files). Maximum file size is
5 TB when using multipart upload.

s3fs is stable and is being used in number of production environments, e.g.,
rsync backup to s3.

%prep
%autosetup -p1

%build
cp -p %{SOURCE1} passwd-s3fs
./autogen.sh
%configure
%make_build

%install
%make_install

%files
%{_bindir}/s3fs
%{_mandir}/man1/s3fs.1*
%doc AUTHORS README.md ChangeLog passwd-s3fs
%{!?_licensedir:%global license %doc}
%license COPYING

%changelog
* Sat Oct 26 2024 Julio González Gil <packages@juliogonzalez.es> - 1.95-1
- Update to 1.95 from https://github.com/s3fs-fuse/s3fs-fuse/releases/tag/v1.95 (#2321940)
  * IMPORTANT: This is the last release supporting CentOS7 or clones
  * Add ipresolve option to select IPv4 or IPv6-only
  * Retry request on HTTP 429 error
  * Fix deadlock in FdManager::ChangeEntityToTempPath
  * Enable static lock checking and fix locking errors
  * Fix use-after-free in FdManager::ChangeEntityToTempPath

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.94-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Feb 29 2024 Julio González Gil <packages@juliogonzalez.es> - 1.94-1
- Update to 1.94 from https://github.com/s3fs-fuse/s3fs-fuse/releases/tag/v1.94 (#2265969)

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.93-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jul 25 2023 Julio González Gil <packages@juliogonzalez.es> - 1.93-1
- Update to 1.93 from https://github.com/s3fs-fuse/s3fs-fuse (#2209081)

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 23 2023 Julio González Gil <packages@juliogonzalez.es> - 1.92-1
- Update to 1.92 from https://github.com/s3fs-fuse/s3fs-fuse (#2209081)
  Full changelog: https://github.com/s3fs-fuse/s3fs-fuse/releases/tag/v1.92

* Mon Apr 17 2023 Julio González Gil <packages@juliogonzalez.es> - 1.91-4
- Adjust the License tag to a valid SPDX expression

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.91-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Mar  8 2022 Julio González Gil <packages@juliogonzalez.es> - 1.91-1
- Update to 1.91 from https://github.com/s3fs-fuse/s3fs-fuse (#2061848)
  Full changelog: https://github.com/s3fs-fuse/s3fs-fuse/releases/tag/v1.91

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.90-2
- Rebuilt with OpenSSL 3.0.0

* Tue Aug 10 2021 Julio González Gil <packages@juliogonzalez.es> - 1.90-1
- Update to 1.90 from https://github.com/s3fs-fuse/s3fs-fuse (#1991301)
  Full changelog: https://github.com/s3fs-fuse/s3fs-fuse/releases/tag/v1.90

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.89-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 24 2021 Julio González Gil <packages@juliogonzalez.es> - 1.89-1
- Update to 1.89 from https://github.com/s3fs-fuse/s3fs-fuse (#1932107)
  Full changelog: https://github.com/s3fs-fuse/s3fs-fuse/releases/tag/v1.89

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.88-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Julio González Gil <packages@juliogonzalez.es> - 1.88-1
- Update to 1.88 from https://github.com/s3fs-fuse/s3fs-fuse (#1914881)
  Full changelog: https://github.com/s3fs-fuse/s3fs-fuse/releases/tag/v1.88

* Mon Aug 10 2020 Julio Gonzalez Gil <packages@juliogonzalez.es> - 1.87-1
- Update to 1.87 from https://github.com/s3fs-fuse/s3fs-fuse (#1867722)
  Full changelog: https://github.com/s3fs-fuse/s3fs-fuse/releases/tag/v1.87

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.86-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 18 2020 Julio Gonzalez Gil <packages@juliogonzalez.es> - 1.86-2
- Add mailcap dependency removed at 1.84-2. as it is in fact a runtime
  dependency to take care of mime-types on upload
  https://github.com/s3fs-fuse/s3fs-fuse/issues/1217

* Wed Feb 05 2020 Julio Gonzalez Gil <git@juliogonzalez.es> - 1.86-1
- Update to 1.86 from https://github.com/s3fs-fuse/s3fs-fuse (#1798716)
  Full changelog: https://github.com/s3fs-fuse/s3fs-fuse/releases/tag/v1.86
- Removed:
  * 985-fix-cross-building.patch
  * 987-support-curl-lt-7-25.patch

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.85-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.85-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 12 2019 Julio Gonzalez Gil <git@juliogonzalez.es> - 1.85-1
- Fix cross building (https://github.com/s3fs-fuse/s3fs-fuse/pull/985)
  * 985-fix-cross-building.patch
- Support Curl lower than 7.25 (CentOS6) (https://github.com/s3fs-fuse/s3fs-fuse/pull/987)
  * 987-support-curl-lt-7-25.patch
- Update to 1.85 from https://github.com/s3fs-fuse/s3fs-fuse
  Full changelog: https://github.com/s3fs-fuse/s3fs-fuse/releases/tag/v1.85

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.84-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 14 2018 Julio Gonzalez Gil <git@juliogonzalez.es> - 1.84-3
- Require fuse package on runtime to allow mounting with systemd,
  mount command or /etc/fstab (#1637669)

* Sat Sep 22 2018 Julio Gonzalez Gil <git@juliogonzalez.es> - 1.84-2
- General cleanup to adapt to Fedora guidelines
- Build with PIE enabled (required by Fedora)
- Remove unneeded build requirement for mailcap

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
