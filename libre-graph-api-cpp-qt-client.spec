%define _empty_manifest_terminate_build 0
Name:           libre-graph-api-cpp-qt-client
Version:        1.0.4
Release:        1
Summary:        Libre Graph Cloud Collaboration API
License:        Apache-2.0
URL:            https://owncloud.dev/libre-graph-api/
Source:         https://github.com/owncloud/libre-graph-api-cpp-qt-client/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  qt5-qtbase-devel

%description
Libre Graph API

API version: v1.0.1
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 
%prep
%autosetup -p1

%build
pushd client
%cmake
%make_build

%install
pushd client
%make_install -C build

%files
%{_includedir}/OpenAPI/
%{_prefix}/lib/cmake/
%{_prefix}/lib/libLibreGraphAPI.a
