/*
Copyright 2008-2022 Thomas Paviot (tpaviot@gmail.com)

This file is part of pythonOCC.
pythonOCC is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pythonOCC is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with pythonOCC.  If not, see <http://www.gnu.org/licenses/>.
*/
%define XMLMDFDOCSTRING
"XmlMDF module, see official documentation at
https://www.opencascade.com/doc/occt-7.6.0/refman/html/package_xmlmdf.html"
%enddef
%module (package="OCC.Core", docstring=XMLMDFDOCSTRING) XmlMDF


%{
#ifdef WNT
#pragma warning(disable : 4716)
#endif
%}

%include ../common/CommonIncludes.i
%include ../common/ExceptionCatcher.i
%include ../common/FunctionTransformers.i
%include ../common/EnumTemplates.i
%include ../common/Operators.i
%include ../common/OccHandle.i


%{
#include<XmlMDF_module.hxx>

//Dependencies
#include<Standard_module.hxx>
#include<NCollection_module.hxx>
#include<Message_module.hxx>
#include<TDF_module.hxx>
#include<XmlObjMgt_module.hxx>
#include<TCollection_module.hxx>
#include<Resource_module.hxx>
#include<TColgp_module.hxx>
#include<TColStd_module.hxx>
#include<TCollection_module.hxx>
#include<Storage_module.hxx>
%};
%import Standard.i
%import NCollection.i
%import Message.i
%import TDF.i
%import XmlObjMgt.i
%import TCollection.i

%pythoncode {
from enum import IntEnum
from OCC.Core.Exception import *
};

/* public enums */
/* end public enums declaration */

/* python proxy classes for enums */
%pythoncode {
};
/* end python proxy for enums */

/* handles */
%wrap_handle(XmlMDF_ADriver)
%wrap_handle(XmlMDF_ADriverTable)
%wrap_handle(XmlMDF_DerivedDriver)
%wrap_handle(XmlMDF_ReferenceDriver)
%wrap_handle(XmlMDF_TagSourceDriver)
/* end handles declaration */

/* templates */
%template(XmlMDF_MapOfDriver) NCollection_DataMap<TCollection_AsciiString,opencascade::handle<XmlMDF_ADriver>,TCollection_AsciiString>;
%template(XmlMDF_TypeADriverMap) NCollection_DataMap<opencascade::handle<Standard_Type>,opencascade::handle<XmlMDF_ADriver>,TColStd_MapTransientHasher>;
/* end templates declaration */

/* typedefs */
typedef NCollection_DataMap<TCollection_AsciiString, opencascade::handle<XmlMDF_ADriver>, TCollection_AsciiString>::Iterator XmlMDF_DataMapIteratorOfMapOfDriver;
typedef NCollection_DataMap<opencascade::handle<Standard_Type>, opencascade::handle<XmlMDF_ADriver>, TColStd_MapTransientHasher>::Iterator XmlMDF_DataMapIteratorOfTypeADriverMap;
typedef NCollection_DataMap<TCollection_AsciiString, opencascade::handle<XmlMDF_ADriver>, TCollection_AsciiString> XmlMDF_MapOfDriver;
typedef NCollection_DataMap<opencascade::handle<Standard_Type>, opencascade::handle<XmlMDF_ADriver>, TColStd_MapTransientHasher> XmlMDF_TypeADriverMap;
/* end typedefs declaration */

/***************
* class XmlMDF *
***************/
%rename(xmlmdf) XmlMDF;
class XmlMDF {
	public:
		/****************** AddDrivers ******************/
		/**** md5 signature: a036f2e24a6710bf8e540cdbbab785d0 ****/
		%feature("compactdefaultargs") AddDrivers;
		%feature("autodoc", "Adds the attribute storage drivers to <adriverseq>.

Parameters
----------
aDriverTable: XmlMDF_ADriverTable
theMessageDriver: Message_Messenger

Returns
-------
None
") AddDrivers;
		static void AddDrivers(const opencascade::handle<XmlMDF_ADriverTable> & aDriverTable, const opencascade::handle<Message_Messenger> & theMessageDriver);

		/****************** FromTo ******************/
		/**** md5 signature: a3040a924b785778b3b8d9cd67f304da ****/
		%feature("compactdefaultargs") FromTo;
		%feature("autodoc", "Translates a transient <asource> into a persistent <atarget>.

Parameters
----------
aSource: TDF_Data
aTarget: XmlObjMgt_Element
aReloc: XmlObjMgt_SRelocationTable
aDrivers: XmlMDF_ADriverTable
theRange: Message_ProgressRange,optional
	default value is Message_ProgressRange()

Returns
-------
None
") FromTo;
		static void FromTo(const opencascade::handle<TDF_Data> & aSource, XmlObjMgt_Element & aTarget, XmlObjMgt_SRelocationTable & aReloc, const opencascade::handle<XmlMDF_ADriverTable> & aDrivers, const Message_ProgressRange & theRange = Message_ProgressRange());

		/****************** FromTo ******************/
		/**** md5 signature: 43d72ef2a4051857449b6205abaf10a8 ****/
		%feature("compactdefaultargs") FromTo;
		%feature("autodoc", "Translates a persistent <asource> into a transient <atarget>. returns true if completed successfully (false on error).

Parameters
----------
aSource: XmlObjMgt_Element
aTarget: TDF_Data
aReloc: XmlObjMgt_RRelocationTable
aDrivers: XmlMDF_ADriverTable
theRange: Message_ProgressRange,optional
	default value is Message_ProgressRange()

Returns
-------
bool
") FromTo;
		static Standard_Boolean FromTo(const XmlObjMgt_Element & aSource, opencascade::handle<TDF_Data> & aTarget, XmlObjMgt_RRelocationTable & aReloc, const opencascade::handle<XmlMDF_ADriverTable> & aDrivers, const Message_ProgressRange & theRange = Message_ProgressRange());

};


%extend XmlMDF {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/***********************
* class XmlMDF_ADriver *
***********************/
%nodefaultctor XmlMDF_ADriver;
class XmlMDF_ADriver : public Standard_Transient {
	public:
		/****************** MessageDriver ******************/
		/**** md5 signature: a2961f713aaae0ef5d0be03881abc817 ****/
		%feature("compactdefaultargs") MessageDriver;
		%feature("autodoc", "Returns the current message driver of this driver.

Returns
-------
opencascade::handle<Message_Messenger>
") MessageDriver;
		const opencascade::handle<Message_Messenger> & MessageDriver();

		/****************** Namespace ******************/
		/**** md5 signature: ed4e20f1f838f6275fc120673f93975a ****/
		%feature("compactdefaultargs") Namespace;
		%feature("autodoc", "Returns the namespace string.

Returns
-------
TCollection_AsciiString
") Namespace;
		const TCollection_AsciiString & Namespace();

		/****************** NewEmpty ******************/
		/**** md5 signature: 537251aec6cd2736ac1f1abe6868dc70 ****/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "Creates a new attribute from tdf.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		virtual opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		/**** md5 signature: 9ba11d4291f863a0ebfa7adc5ddc82da ****/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "Translate the contents of <asource> and put it into <atarget>, using the relocation table <areloctable> to keep the sharings.

Parameters
----------
aSource: XmlObjMgt_Persistent
aTarget: TDF_Attribute
aRelocTable: XmlObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		virtual Standard_Boolean Paste(const XmlObjMgt_Persistent & aSource, const opencascade::handle<TDF_Attribute> & aTarget, XmlObjMgt_RRelocationTable & aRelocTable);

		/****************** Paste ******************/
		/**** md5 signature: 52806332c1e637e234838754c7c1b878 ****/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "Translate the contents of <asource> and put it into <atarget>, using the relocation table <areloctable> to keep the sharings.

Parameters
----------
aSource: TDF_Attribute
aTarget: XmlObjMgt_Persistent
aRelocTable: XmlObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		virtual void Paste(const opencascade::handle<TDF_Attribute> & aSource, XmlObjMgt_Persistent & aTarget, XmlObjMgt_SRelocationTable & aRelocTable);

		/****************** SourceType ******************/
		/**** md5 signature: 32631522887e31f15896a5cd3347c279 ****/
		%feature("compactdefaultargs") SourceType;
		%feature("autodoc", "Returns the type of source object, inheriting from attribute from tdf.

Returns
-------
opencascade::handle<Standard_Type>
") SourceType;
		virtual opencascade::handle<Standard_Type> SourceType();

		/****************** TypeName ******************/
		/**** md5 signature: 191a1aa753fb8d39d56bcfd7505ea0e7 ****/
		%feature("compactdefaultargs") TypeName;
		%feature("autodoc", "Returns the full xml tag name (including ns prefix).

Returns
-------
TCollection_AsciiString
") TypeName;
		const TCollection_AsciiString & TypeName();

		/****************** VersionNumber ******************/
		/**** md5 signature: debfb90d077419555d82ec5a7fb62cea ****/
		%feature("compactdefaultargs") VersionNumber;
		%feature("autodoc", "Returns the version number from which the driver is available.

Returns
-------
int
") VersionNumber;
		virtual Standard_Integer VersionNumber();

};


%make_alias(XmlMDF_ADriver)

%extend XmlMDF_ADriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/****************************
* class XmlMDF_ADriverTable *
****************************/
class XmlMDF_ADriverTable : public Standard_Transient {
	public:
		/****************** XmlMDF_ADriverTable ******************/
		/**** md5 signature: 019227b2f290ebee141aefb3a01e3eae ****/
		%feature("compactdefaultargs") XmlMDF_ADriverTable;
		%feature("autodoc", "Creates a mutable adrivertable from xmlmdf.

Returns
-------
None
") XmlMDF_ADriverTable;
		 XmlMDF_ADriverTable();

		/****************** AddDerivedDriver ******************/
		/**** md5 signature: d785bc7c368abacc51e9bcd52083ce5c ****/
		%feature("compactdefaultargs") AddDerivedDriver;
		%feature("autodoc", "Adds a translation driver for the derived attribute. the base driver must be already added. @param theinstance is newly created attribute, detached from any label.

Parameters
----------
theInstance: TDF_Attribute

Returns
-------
None
") AddDerivedDriver;
		void AddDerivedDriver(const opencascade::handle<TDF_Attribute> & theInstance);

		/****************** AddDerivedDriver ******************/
		/**** md5 signature: c08557200bb111bac7324de5048e9e2d ****/
		%feature("compactdefaultargs") AddDerivedDriver;
		%feature("autodoc", "Adds a translation driver for the derived attribute. the base driver must be already added. @param thederivedtype is registered attribute type using implement_derived_attribute macro.

Parameters
----------
theDerivedType: str

Returns
-------
opencascade::handle<Standard_Type>
") AddDerivedDriver;
		const opencascade::handle<Standard_Type> & AddDerivedDriver(Standard_CString theDerivedType);

		/****************** AddDriver ******************/
		/**** md5 signature: a1862a3b70afac69a2082adfc7eb62a0 ****/
		%feature("compactdefaultargs") AddDriver;
		%feature("autodoc", "Sets a translation driver: <adriver>.

Parameters
----------
anHDriver: XmlMDF_ADriver

Returns
-------
None
") AddDriver;
		void AddDriver(const opencascade::handle<XmlMDF_ADriver> & anHDriver);

		/****************** CreateDrvMap ******************/
		/**** md5 signature: 2f3bf75f266927cb151a797b3ee15dcf ****/
		%feature("compactdefaultargs") CreateDrvMap;
		%feature("autodoc", "Fills the map by all registered drivers.

Parameters
----------
theDriverMap: XmlMDF_MapOfDriver

Returns
-------
None
") CreateDrvMap;
		void CreateDrvMap(XmlMDF_MapOfDriver & theDriverMap);

		/****************** GetDriver ******************/
		/**** md5 signature: 82134288246a0f36c04a3a279ed39cd1 ****/
		%feature("compactdefaultargs") GetDriver;
		%feature("autodoc", "Gets a driver <adriver> according to <atype> //! returns true if a driver is found; false otherwise.

Parameters
----------
theType: Standard_Type
theDriver: XmlMDF_ADriver

Returns
-------
bool
") GetDriver;
		Standard_Boolean GetDriver(const opencascade::handle<Standard_Type> & theType, opencascade::handle<XmlMDF_ADriver> & theDriver);

};


%make_alias(XmlMDF_ADriverTable)

%extend XmlMDF_ADriverTable {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/*****************************
* class XmlMDF_DerivedDriver *
*****************************/
class XmlMDF_DerivedDriver : public XmlMDF_ADriver {
	public:
		/****************** XmlMDF_DerivedDriver ******************/
		/**** md5 signature: 9fd7a0ae1dfaceed6d0fe854211abbae ****/
		%feature("compactdefaultargs") XmlMDF_DerivedDriver;
		%feature("autodoc", "Creates a derivative persistence driver for thederivative attribute by reusage of thebasedriver @param thederivative an instance of the attribute, just created, detached from any label @param thebasedriver a driver of the base attribute, called by paste methods.

Parameters
----------
theDerivative: TDF_Attribute
theBaseDriver: XmlMDF_ADriver

Returns
-------
None
") XmlMDF_DerivedDriver;
		 XmlMDF_DerivedDriver(const opencascade::handle<TDF_Attribute> & theDerivative, const opencascade::handle<XmlMDF_ADriver> & theBaseDriver);

		/****************** NewEmpty ******************/
		/**** md5 signature: 9fd03ebf4c88d0fd3efd748ca3107174 ****/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "Creates a new instance of the derivative attribute.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		virtual opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		/**** md5 signature: ec1aa8d8f44b52c462ccfb619b2ab8c7 ****/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "Reuses the base driver to read the base fields.

Parameters
----------
theSource: XmlObjMgt_Persistent
theTarget: TDF_Attribute
theRelocTable: XmlObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		virtual Standard_Boolean Paste(const XmlObjMgt_Persistent & theSource, const opencascade::handle<TDF_Attribute> & theTarget, XmlObjMgt_RRelocationTable & theRelocTable);

		/****************** Paste ******************/
		/**** md5 signature: 50bb20461c6c07de84069a8198f95fcd ****/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "Reuses the base driver to store the base fields.

Parameters
----------
theSource: TDF_Attribute
theTarget: XmlObjMgt_Persistent
theRelocTable: XmlObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		virtual void Paste(const opencascade::handle<TDF_Attribute> & theSource, XmlObjMgt_Persistent & theTarget, XmlObjMgt_SRelocationTable & theRelocTable);

		/****************** TypeName ******************/
		/**** md5 signature: 33bd6dc5f76c10259f99124470e7cb5c ****/
		%feature("compactdefaultargs") TypeName;
		%feature("autodoc", "Returns the full xml tag name (including ns prefix).

Returns
-------
TCollection_AsciiString
") TypeName;
		const TCollection_AsciiString & TypeName();

};


%make_alias(XmlMDF_DerivedDriver)

%extend XmlMDF_DerivedDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/*******************************
* class XmlMDF_ReferenceDriver *
*******************************/
class XmlMDF_ReferenceDriver : public XmlMDF_ADriver {
	public:
		/****************** XmlMDF_ReferenceDriver ******************/
		/**** md5 signature: b53c8eb2906d5bbe7f077cd2090ccdd0 ****/
		%feature("compactdefaultargs") XmlMDF_ReferenceDriver;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMessageDriver: Message_Messenger

Returns
-------
None
") XmlMDF_ReferenceDriver;
		 XmlMDF_ReferenceDriver(const opencascade::handle<Message_Messenger> & theMessageDriver);

		/****************** NewEmpty ******************/
		/**** md5 signature: c6d13c9ecc64c6c803b6e119e8216934 ****/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		/**** md5 signature: 3dd41285e4a0d4dafa2b2b321d4fcc26 ****/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: XmlObjMgt_Persistent
Target: TDF_Attribute
RelocTable: XmlObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		Standard_Boolean Paste(const XmlObjMgt_Persistent & Source, const opencascade::handle<TDF_Attribute> & Target, XmlObjMgt_RRelocationTable & RelocTable);

		/****************** Paste ******************/
		/**** md5 signature: bfb59b0a8136ec850943b5ad7848f316 ****/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: TDF_Attribute
Target: XmlObjMgt_Persistent
RelocTable: XmlObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		void Paste(const opencascade::handle<TDF_Attribute> & Source, XmlObjMgt_Persistent & Target, XmlObjMgt_SRelocationTable & RelocTable);

};


%make_alias(XmlMDF_ReferenceDriver)

%extend XmlMDF_ReferenceDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/*******************************
* class XmlMDF_TagSourceDriver *
*******************************/
class XmlMDF_TagSourceDriver : public XmlMDF_ADriver {
	public:
		/****************** XmlMDF_TagSourceDriver ******************/
		/**** md5 signature: c41a1e34cf012a6f231ee5225f896395 ****/
		%feature("compactdefaultargs") XmlMDF_TagSourceDriver;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMessageDriver: Message_Messenger

Returns
-------
None
") XmlMDF_TagSourceDriver;
		 XmlMDF_TagSourceDriver(const opencascade::handle<Message_Messenger> & theMessageDriver);

		/****************** NewEmpty ******************/
		/**** md5 signature: c6d13c9ecc64c6c803b6e119e8216934 ****/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		/**** md5 signature: 3dd41285e4a0d4dafa2b2b321d4fcc26 ****/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: XmlObjMgt_Persistent
Target: TDF_Attribute
RelocTable: XmlObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		Standard_Boolean Paste(const XmlObjMgt_Persistent & Source, const opencascade::handle<TDF_Attribute> & Target, XmlObjMgt_RRelocationTable & RelocTable);

		/****************** Paste ******************/
		/**** md5 signature: bfb59b0a8136ec850943b5ad7848f316 ****/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: TDF_Attribute
Target: XmlObjMgt_Persistent
RelocTable: XmlObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		void Paste(const opencascade::handle<TDF_Attribute> & Source, XmlObjMgt_Persistent & Target, XmlObjMgt_SRelocationTable & RelocTable);

};


%make_alias(XmlMDF_TagSourceDriver)

%extend XmlMDF_TagSourceDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/* harray1 classes */
/* harray2 classes */
/* hsequence classes */
/* class aliases */
%pythoncode {
}
/* deprecated methods */
%pythoncode {
@deprecated
def xmlmdf_AddDrivers(*args):
	return xmlmdf.AddDrivers(*args)

@deprecated
def xmlmdf_FromTo(*args):
	return xmlmdf.FromTo(*args)

@deprecated
def xmlmdf_FromTo(*args):
	return xmlmdf.FromTo(*args)

}
