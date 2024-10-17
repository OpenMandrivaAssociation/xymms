Summary:	GYM Input plugin for XMMS
Name:		xymms
Version:	0.9.1
Release: %mkrel 8
License:	BSD
Group:		Sound
URL:		https://sourceforge.net/projects/xymms/
Source:		%{name}-%{version}.tar.bz2
BuildRequires:	xmms-devel
BuildRequires:	zlib-devel
BuildRequires:	automake
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
XymMS is an XMMS input plugin capable of playing Sega Genesis GYM files by
rendering FM, DAC, and PSG signals through emulation of the YM2612 and SN76496
sound chips found in the video game console. (CYM files will be supported in
the beta release.) GYM files are created by various emulators such as DGen and
Megasis. XymMS supports ZLib compression and decompression, and other various
settings for output quality, etc. You can compress and decompress files along
with updating ID tags using the File Info window. The emulation backend is
courtesy the M.A.M.E. project. XymMS is based on code and ideas from the YMAMP
and MSP Open Source projects.

%prep

%setup -q
autoreconf -fi

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%{_libdir}/xmms/Input/libxymms.*a

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING README AUTHORS README.MAME
%{_libdir}/xmms/Input/libxymms.so

