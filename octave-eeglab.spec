%define octpkg eeglab

Summary:	A signal processing environment for electrophysiological signals for Octave
Name:		octave-%{octpkg}
Version:	2022.1
Release:	1
Source0:	https://github.com/sccn/%{octpkg}/archive/%{version}/%{octpkg}-%{version}.tar.gz
License:	BSD
Group:		Sciences/Mathematics
Url:		https://eeglab.ucsd.edu

BuildRequires:	octave-devel >= 4.0.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
EEGLAB is an open source signal processing environment for electrophysiological
signals running on Matlab and Octave (command line only for Octave). This folder
contains original Matlab functions from the EEGLAB (formerly ICA/EEG) Matlab
toolbox, all released under the Gnu public license (see eeglablicence.txt).

See the EEGLAB tutorial and reference paper for more information.

%files
%license COPYING
#doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# fix file paths
mkdir inst
mkdir src
mv *.m inst
touch COPYING
cat >DESCRIPTION <<EOF
Name: %{octpkg}
Version: %{version}
Date: 2022-08-01
Author: Arnaud Delorme, Scott Makeig Tran, Colin Humphries, Sigurd Enghoff, Tzyy-Ping Jung, Tony Bell, Te-Won Lee, Luca Finelli
Maintainer: Qianqian Fang <q.fang at neu.edu>
Title: EEGLAB
Description: %{summary}.
Depends: octave (>= 4.0.0)
Autoload: no
License: BSD
Categories: electroencephalogram
EOF

# remove backup files
#find . -name \*~ -delete

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

