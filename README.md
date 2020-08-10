s3fs-fuse
=========

<table padding="0">
  <tr>
    <th colspan="2">Statuses</th>
  </tr>
  <tr>
    <td>Tests and RPM Builds<br />(CentOS7, Amazon Linux 2017.03)</td>
    <td>
      <a href="https://jenkins.juliogonzalez.es/job/s3fs-fuse-rpm-build/" target="_blank"><img src="https://jenkins.juliogonzalez.es/job/s3fs-fuse-rpm-build/badge/icon" alt="Test status" valign="middle" /></a>
    </td>
  </tr>
  <tr>
    <td>COPR RPM Builds<br />(Fedora and EPEL7)</td>
    <td>
      <a href="https://copr.fedorainfracloud.org/coprs/juliogonzalez/s3fs-fuse/monitor/" target="_blank"><img src="https://copr.fedorainfracloud.org/coprs/juliogonzalez/s3fs-fuse/package/s3fs-fuse/status_image/last_build.png" alt="RPM Build status" valign="middle" /></a>
    </td>
  </tr>
</table>

CentOS/RH/Amazon RPMs for s3fs <https://github.com/s3fs-fuse/s3fs-fuse>

Based off the [spec file](http://kad.fedorapeople.org/packages/s3fs/s3fs.spec) created by [Jorge A Gallegos](http://kad.fedorapeople.org/), referenced at <https://bugzilla.redhat.com/show_bug.cgi?id=725292>, and upgraded by [Corey Gilmore](https://github.com/cfg), refered at <https://github.com/cfg/s3fs>


Tested on x64 CentOS 7 and Amazon Linux 2017.03

**WARNING**: CentOS6/RHEL6 are **not** supported since s3fs v1.87 as discussed at https://github.com/s3fs-fuse/s3fs-fuse/issues/1354 If you still want to use s3fs, use [v1.86-2](https://github.com/juliogonzalez/s3fs-fuse-rpm/releases/tag/1.86-2)

Source for Fedora and EPEL
--------------------------

As of today, the SPEC in this repository is exactly the same that is then pushed to the [Fedora Project](https://src.fedoraproject.org/rpms/s3fs-fuse/) to generate the [submissions to Fedora and EPEL](https://bodhi.fedoraproject.org/updates/?packages=s3fs-fuse)


Build Requirements
------------------

* automake
* curl
* make
* fuse-devel (>= 2.8.4)
* git (to clone this repository, not needed if you download a tarball from the [releases](https://github.com/juliogonzalez/s3fs-fuse-rpm/releases))
* gcc-c++
* libcurl-devel
* libxml2-devel
* make
* openssl-devel
* pkgconfig
* rpm-build

Building fresh RPMs
-------------------

Clone the repo:

    git@github.com:juliogonzalez/s3fs-fuse-rpm.git
    cd s3fs-fuse-rpm


Build the s3fs-fuse RPMs
------------------------

Build the RPMs:

    ./s3fs-build-rpm

And install:

    rpm -Uvh RPMS/$HOSTTYPE/s3fs-fuse-1.87-1.*.$HOSTTYPE.rpm
