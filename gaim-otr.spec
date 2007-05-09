%define	version	3.0.0
%define release	%mkrel 3

Summary:	GAIM plugin that implements Off-the-Record Messaging
Name:		gaim-otr
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Networking/Instant messaging
URL:		http://www.cypherpunks.ca/otr/
Source0:	http://www.cypherpunks.ca/otr/%{name}-%{version}.tar.gz
Source1:	http://www.cypherpunks.ca/otr/%{name}-%{version}.tar.gz.asc
Patch0:		gaim-otr-3.0.0-gaim2beta.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gaim-devel
BuildRequires:	libotr-devel >= 3.0.0
BuildRequires:	gtk2-devel >= 2.4
BuildRequires:	libgcrypt-devel >= 1.2.0
Requires:	gaim

%description
This is a plugin for gaim 1.x which implements Off-the-Record
Messaging over any IM network gaim supports.

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
%patch0 -p1 -b .gaim2beta

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# remove unneeded file
rm -f %{buildroot}%{_libdir}/gaim/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/gaim/*.so


