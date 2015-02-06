Name:		toilet
Version:	0.2
Release:	3
Summary:	Powerful figlet replacement
License:	WTFPL
Group:		Text tools
Url:		http://libcaca.zoy.org/toilet.html
Source:		http://libcaca.zoy.org/files/%{name}-%{version}.tar.gz
BuildRequires:	libcaca-devel zlib-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

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
./bootstrap
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


%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2-2mdv2011.0
+ Revision: 615233
- the mass rebuild of 2010.1 packages

* Sun Feb 14 2010 Pascal Terjan <pterjan@mandriva.org> 0.2-1mdv2010.1
+ Revision: 505675
- 0.2

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.1-5mdv2010.0
+ Revision: 445495
- rebuild

* Fri Nov 14 2008 Pascal Terjan <pterjan@mandriva.org> 0.1-4mdv2009.1
+ Revision: 303147
- Fix build with as-needed
- Add upstream patch fixing build with --as-needed

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

* Wed Mar 26 2008 Pascal Terjan <pterjan@mandriva.org> 0.1-1mdv2008.1
+ Revision: 190248
- import toilet


