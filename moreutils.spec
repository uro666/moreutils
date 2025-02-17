Name:		moreutils
Version:	0.70
Release:	1
Source0:	https://git.joeyh.name/index.cgi/moreutils.git/snapshot/%{name}-%{version}.tar.gz
Summary:	a collection of unix tools
URL:		https://joeyh.name/code/moreutils/
License:	GPLv2
Group:		System/Utils
BuildRequires:	make
BuildRequires:	docbook-dtds
BuildRequires:	libxml2-utils
BuildRequires:	xsltproc
Requires:	perl-IPC-Run


%description 
additional Unix utilities

 This is a growing collection of the Unix tools that nobody
 thought to write long ago, when Unix was young.

 So far, it includes the following utilities:
  - chronic: runs a command quietly unless it fails
  - combine: combine the lines in two files using boolean operations
  - errno: look up errno names and descriptions
  - ifdata: get network interface info without parsing ifconfig output
  - ifne: run a program if the standard input is not empty
  - isutf8: check if a file or standard input is utf-8
  - lckdo: execute a program with a lock held
  - mispipe: pipe two commands, returning the exit status of the first
  - parallel: run multiple jobs at once
  - pee: tee standard input to pipes
  - sponge: soak up standard input and write to a file
  - ts: timestamp standard input
  - vidir: edit a directory in your text editor
  - vipe: insert a text editor into a pipe
  - zrun: automatically uncompress arguments to command

%global debug_package %{nil}

%prep
%autosetup -p1

%build
%make_build \
	DOCBOOKXSL?=/usr/share/sgml/docbook/xsl-stylesheets

%install
%make_install \
	DOCBOOKXSL?=/usr/share/sgml/docbook/xsl-stylesheets

%files
%doc debian/changelog
%doc COPYING
%doc README
%doc %{_mandir}/man1/*.1*
%{_bindir}/*
