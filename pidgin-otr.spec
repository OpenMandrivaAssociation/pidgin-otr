%define _disable_ld_no_undefined 1

Summary:	Pidgin plugin that implements Off-the-Record Messaging
Name:		pidgin-otr
Version:	4.0.0
Release:	1
License:	GPLv2+
Group:		Networking/Instant messaging
Url:		http://www.cypherpunks.ca/otr/
Source0:	http://www.cypherpunks.ca/otr/%{name}-%{version}.tar.gz
Source1:	http://www.cypherpunks.ca/otr/%{name}-%{version}.tar.gz.asc
BuildRequires:	intltool
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(libotr)
BuildRequires:	pkgconfig(pidgin)
Requires:	pidgin

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

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/pidgin/*.so

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

# remove unneeded file
rm -f %{buildroot}%{_libdir}/pidgin/*.la

%find_lang %{name}

