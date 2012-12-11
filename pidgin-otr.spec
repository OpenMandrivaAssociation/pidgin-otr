%define	version	3.2.1
%define release	%mkrel 2

Summary:	Pidgin plugin that implements Off-the-Record Messaging
Name:		pidgin-otr
Version:	%{version}
Release:	%{release}
License:	GPLv2
Group:		Networking/Instant messaging
URL:		http://www.cypherpunks.ca/otr/
Source0:	http://www.cypherpunks.ca/otr/%{name}-%{version}.tar.gz
Source1:	http://www.cypherpunks.ca/otr/%{name}-%{version}.tar.gz.asc
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	pidgin-devel
BuildRequires:	libotr-devel >= 3.2.0-5.1
BuildRequires:	gtk2-devel >= 2.4
BuildRequires:	libgcrypt-devel >= 1.2.0
BuildRequires:	intltool
Requires:	pidgin
Provides: gaim-otr
Obsoletes: gaim-otr

%description
This is a plugin for pidgin which implements Off-the-Record
Messaging over any IM network pidgin supports.

OTR allows you to have private conversations over IM by providing:
 - Encryption
   - No one else can read your instant messages.
 - Authentication
   - You are assured the correspondent is who you think it is.
 - Deniability
   - The messages you send do _not_ have digital signatures that are
     checkable by a third party.  Anyone can forge messages after a
     conversation to make them look like they came from you.  However,
     _during_ a conversation, your correspondent is assured the messages
     he sees are authentic and unmodified.
 - Perfect forward secrecy
   - If you lose control of your private keys, no previous conversation
     is compromised.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot} %name.lang
%makeinstall_std

# remove unneeded file
rm -f %{buildroot}%{_libdir}/pidgin/*.la

%find_lang %name

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/pidgin/*.so




%changelog
* Mon Aug 20 2012 Götz Waschk <waschk@mandriva.org> 3.2.1-2mdv2012.0
+ Revision: 815454
- rebuild

* Wed Aug 15 2012 Götz Waschk <waschk@mandriva.org> 3.2.1-1
+ Revision: 814850
- add build dep on intltool
- drop patch
- relax libotr version, allow build with the security update
- update to new version 3.2.1

* Wed Jul 13 2011 Götz Waschk <waschk@mandriva.org> 3.2.0-3
+ Revision: 689837
- rebuild

* Sun Jun 21 2009 Götz Waschk <waschk@mandriva.org> 3.2.0-2mdv2011.0
+ Revision: 387918
- fix format string
- update license

* Sat Jun 21 2008 Funda Wang <fwang@mandriva.org> 3.2.0-1mdv2009.0
+ Revision: 227776
- New version 3.2.0

* Thu Mar 13 2008 Andreas Hasenack <andreas@mandriva.com> 3.1.0-3mdv2008.1
+ Revision: 187588
- rebuild for 2008.1

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Oct 03 2007 Funda Wang <fwang@mandriva.org> 3.1.0-2mdv2008.0
+ Revision: 95086
- rebuild for pidgin 2.2.1

* Mon Aug 06 2007 Götz Waschk <waschk@mandriva.org> 3.1.0-1mdv2008.0
+ Revision: 59295
- fix buildrequires
- new version
- drop patches
- bump deps
- update file list

* Wed May 09 2007 Götz Waschk <waschk@mandriva.org> 3.0.0-1mdv2008.0
+ Revision: 25659
- new version
- patch for pidgin 2.0
- rename

