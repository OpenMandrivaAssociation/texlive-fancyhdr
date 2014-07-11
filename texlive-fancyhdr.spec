# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/fancyhdr
# catalog-date 2009-01-10 12:36:34 +0100
# catalog-license lppl
# catalog-version 3.1
Name:		texlive-fancyhdr
Version:	3.1
Release:	8
Summary:	Extensive control of page headers and footers in LaTeX2e
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fancyhdr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancyhdr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancyhdr.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides extensive facilities, both for
constructing headers and footers, and for controlling their use
(for example, at times when LaTeX would automatically change
the heading style in use).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fancyhdr/extramarks.sty
%{_texmfdistdir}/tex/latex/fancyhdr/fancyhdr.sty
%{_texmfdistdir}/tex/latex/fancyhdr/fancyheadings.sty
%doc %{_texmfdistdir}/doc/latex/fancyhdr/README
%doc %{_texmfdistdir}/doc/latex/fancyhdr/fancyhdr.pdf
%doc %{_texmfdistdir}/doc/latex/fancyhdr/fancyhdr.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.1-2
+ Revision: 751755
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.1-1
+ Revision: 718412
- texlive-fancyhdr
- texlive-fancyhdr
- texlive-fancyhdr
- texlive-fancyhdr

