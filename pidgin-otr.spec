%define	version	3.2.0
%define release	%mkrel 3

Summary:	Pidgin plugin that implements Off-the-Record Messaging
Name:		pidgin-otr
Version:	%{version}
Release:	%{release}
License:	GPLv2
Group:		Networking/Instant messaging
URL:		http://www.cypherpunks.ca/otr/
Source0:	http://www.cypherpunks.ca/otr/%{name}-%{version}.tar.gz
Source1:	http://www.cypherpunks.ca/otr/%{name}-%{version}.tar.gz.asc
Patch:		pidgin-otr-3.2.0-format-string.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	pidgin-devel
BuildRequires:	libotr-devel >= %{version}
BuildRequires:	gtk2-devel >= 2.4
BuildRequires:	libgcrypt-devel >= 1.2.0
BuildRequires:	perl-XML-Parser
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
%patch -p1

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


