Name:		toilet
Version:	0.1
Release:	%mkrel 1
Summary:	Powerful figlet replacement
License:	WTFPL
Group:		Text tools
Url:		http://libcaca.zoy.org/toilet.html
Source:		http://libcaca.zoy.org/files/%{name}-%{version}.tar.gz
BuildRequires:	libcaca-devel zlib-devel

%description
TOIlet is in its very early development phase. It uses the powerful libcucul
library to achieve various text-based effects. TOIlet implements or plans to
implement the following features:
 * The ability to load FIGlet fonts
 * Support for Unicode input and output
 * Support for colour output
 * Support for various output formats: HTML, IRC, ANSI...

TOIlet also aims for full FIGlet compatibility. It is currently able to load
FIGlet fonts and perform horizontal smushing. 

%prep
%setup -q

%build
%configure2_5x
%make

%clean
rm -rf %buildroot

%install
rm -rf %buildroot
%makeinstall 

%files
%_bindir/toilet
%_datadir/figlet
%_mandir/man1/toilet.*