%global octpkg eeglab

Summary:	A signal processing environment for electrophysiological signals for Octave
Name:		octave-eeglab
Version:	2023.1
Release:	1
License:	BSD
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/eeglab/
Url:		https://github.com/sccn/eeglab
Source0:	https://github.com/sccn/eeglab/archive/%{version}/eeglab-%{version}.tar.gz

BuildRequires:  octave-devel >= 6.1.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
An interactive toolbox for processing continuous and event-related
EEG, MEG and other electrophysiological data incorporating
independent component analysis (ICA), time/frequency analysis,
artifact rejection, event-related statistics, and several useful
modes of visualization of the averaged and single-trial data.

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

# add missing files
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


%build
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

