# norootforbuild

Name:           truecrypt
Version:        7.0
Release:        1.0
License:        TrueCrypt License Version 3.0
Group:          Productivity/Security
Url:            http://www.truecrypt.org
Source:         %{name}-%{version}-source.tar.bz2
Patch0:         truecrypt-6.3a-opt_flags.patch
Patch1:         truecrypt-6.3a-compile.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  fuse-devel
BuildRequires:  gcc-c++
BuildRequires:  nasm
BuildRequires:  pkcs11-helper-devel
BuildRequires:  update-desktop-files
BuildRequires:  wxGTK-devel
Summary:        Free Open-Source Disk Encryption Software

%description
TrueCrypt is a software system for establishing and maintaining an on-the-fly-encrypted 
volume (data storage device).

On-the-fly encryption means that data is automatically encrypted or decrypted 
right before it is loaded or saved, without any user intervention.
No data stored on an encrypted volume can be read (decrypted) without using 
the correct password/keyfile(s) or correct encryption keys. 

Entire file system is encrypted (i.e., file names, folder names, contents of 
every file, and free space).


Authors:
--------
 - TrueCrypt Foundation
 - Paul Le Roux
 - Brian Gladman
 - Eric Young
 - Mark Adler
 - Markus Friedl


%prep
%setup -qn truecrypt-%{version}-source
%patch0
%patch1

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
export PKCS11_INC=%{_includedir}/pkcs11-helper-1.0
%__make NOSTRIP=1 VERBOSE=1 %{?_smp_mflags}

%install
%__install -Dm 0755 Main/truecrypt %{buildroot}%{_bindir}/%{name}
%__install -Dm 0644 Resources/Icons/TrueCrypt-16x16.xpm %{buildroot}%{_datadir}/pixmaps/%{name}-16x16.xpm
%__install -Dm 0644 Resources/Icons/TrueCrypt-48x48.xpm %{buildroot}%{_datadir}/pixmaps/%{name}-48x48.xpm
%suse_update_desktop_file -c %{name} "TrueCrypt %{version}" "Free open-source disk encryption software" %{name} %{name}-48x48.xpm Utility Security

%clean
[[ %{buildroot} != "" && %{buildroot} != "/" ]] && %__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Release/Setup\ Files/License.txt Release/Setup\ Files/TrueCrypt\ User\ Guide.pdf
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}-??x??.xpm
