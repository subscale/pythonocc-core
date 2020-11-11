from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Interface import *
from OCC.Core.TColStd import *
from OCC.Core.TopTools import *
from OCC.Core.Message import *
from OCC.Core.Transfer import *
from OCC.Core.TopoDS import *
from OCC.Core.TopAbs import *


class TransferBRep_SequenceOfTransferResultInfo:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> False: ...
    def Last(self) -> False: ...
    def Length(self) -> int: ...
    def Append(self, theItem: False) -> False: ...
    def Prepend(self, theItem: False) -> False: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> False: ...
    def SetValue(self, theIndex: int, theValue: False) -> None: ...

class transferbrep:
	@staticmethod
	def CheckObject(chl: Interface_CheckIterator, obj: Standard_Transient) -> Interface_CheckIterator: ...
	@staticmethod
	def Checked(chl: Interface_CheckIterator, alsoshapes: Optional[bool] = False) -> TColStd_HSequenceOfTransient: ...
	@staticmethod
	def CheckedShapes(chl: Interface_CheckIterator) -> TopTools_HSequenceOfShape: ...
	@staticmethod
	def PrintResultInfo(Printer: Message_Printer, Header: Message_Msg, ResultInfo: TransferBRep_TransferResultInfo, printEmpty: Optional[bool] = True) -> None: ...
	@staticmethod
	def ResultCheckList(chl: Interface_CheckIterator, FP: Transfer_FinderProcess, model: Interface_InterfaceModel) -> Interface_CheckIterator: ...
	@staticmethod
	def ResultFromShape(FP: Transfer_FinderProcess, shape: TopoDS_Shape) -> Transfer_Binder: ...
	@staticmethod
	def SetShapeResult(TP: Transfer_TransientProcess, ent: Standard_Transient, result: TopoDS_Shape) -> None: ...
	@staticmethod
	def SetTransientFromShape(FP: Transfer_FinderProcess, shape: TopoDS_Shape, result: Standard_Transient) -> None: ...
	@staticmethod
	def ShapeMapper(FP: Transfer_FinderProcess, shape: TopoDS_Shape) -> TransferBRep_ShapeMapper: ...
	@overload
	@staticmethod
	def ShapeResult(binder: Transfer_Binder) -> TopoDS_Shape: ...
	@overload
	@staticmethod
	def ShapeResult(TP: Transfer_TransientProcess, ent: Standard_Transient) -> TopoDS_Shape: ...
	@staticmethod
	def ShapeState(FP: Transfer_FinderProcess, shape: TopoDS_Shape) -> TopAbs_Orientation: ...
	@overload
	@staticmethod
	def Shapes(TP: Transfer_TransientProcess, rootsonly: Optional[bool] = True) -> TopTools_HSequenceOfShape: ...
	@overload
	@staticmethod
	def Shapes(TP: Transfer_TransientProcess, list: TColStd_HSequenceOfTransient) -> TopTools_HSequenceOfShape: ...
	@overload
	@staticmethod
	def TransferResultInfo(TP: Transfer_TransientProcess, EntityTypes: TColStd_HSequenceOfTransient, InfoSeq: TransferBRep_HSequenceOfTransferResultInfo) -> None: ...
	@overload
	@staticmethod
	def TransferResultInfo(FP: Transfer_FinderProcess, ShapeTypes: TColStd_HSequenceOfInteger, InfoSeq: TransferBRep_HSequenceOfTransferResultInfo) -> None: ...
	@staticmethod
	def TransientFromShape(FP: Transfer_FinderProcess, shape: TopoDS_Shape) -> Standard_Transient: ...

class TransferBRep_BinderOfShape(Transfer_Binder):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, res: TopoDS_Shape) -> None: ...
	def CResult(self) -> TopoDS_Shape: ...
	def Result(self) -> TopoDS_Shape: ...
	def ResultType(self) -> Standard_Type: ...
	def ResultTypeName(self) -> str: ...
	def SetResult(self, res: TopoDS_Shape) -> None: ...

class TransferBRep_OrientedShapeMapper(Transfer_Finder):
	def __init__(self, akey: TopoDS_Shape) -> None: ...
	def Equates(self, other: Transfer_Finder) -> bool: ...
	def Value(self) -> TopoDS_Shape: ...
	def ValueType(self) -> Standard_Type: ...
	def ValueTypeName(self) -> str: ...

class TransferBRep_Reader:
	def __init__(self) -> None: ...
	def Actor(self) -> Transfer_ActorOfTransientProcess: ...
	def BeginTransfer(self) -> bool: ...
	def CheckListModel(self) -> Interface_CheckIterator: ...
	def CheckListResult(self) -> Interface_CheckIterator: ...
	def CheckStatusModel(self, withprint: bool) -> bool: ...
	def CheckStatusResult(self, withprints: bool) -> bool: ...
	def Clear(self) -> None: ...
	def EndTransfer(self) -> None: ...
	def FileNotFound(self) -> bool: ...
	def FileStatus(self) -> int: ...
	def IsDone(self) -> bool: ...
	def GetModeNewTransfer(self) -> bool: ...
	def SetModeNewTransfer(self, value: bool) -> None: ...
	def Model(self) -> Interface_InterfaceModel: ...
	def NbShapes(self) -> int: ...
	def NbTransients(self) -> int: ...
	def OneShape(self) -> TopoDS_Shape: ...
	def PrepareTransfer(self) -> None: ...
	def Protocol(self) -> Interface_Protocol: ...
	def SetActor(self, actor: Transfer_ActorOfTransientProcess) -> None: ...
	def SetFileStatus(self, status: int) -> None: ...
	def SetModel(self, model: Interface_InterfaceModel) -> None: ...
	def SetProtocol(self, protocol: Interface_Protocol) -> None: ...
	def Shape(self, num: Optional[int] = 1) -> TopoDS_Shape: ...
	def ShapeResult(self, ent: Standard_Transient) -> TopoDS_Shape: ...
	def Shapes(self) -> TopTools_HSequenceOfShape: ...
	def SyntaxError(self) -> bool: ...
	def Transfer(self, num: int, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> bool: ...
	def TransferList(self, list: TColStd_HSequenceOfTransient, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
	def TransferRoots(self, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
	def Transient(self, num: Optional[int] = 1) -> Standard_Transient: ...
	def TransientProcess(self) -> Transfer_TransientProcess: ...
	def Transients(self) -> TColStd_HSequenceOfTransient: ...

class TransferBRep_ShapeInfo:
	@staticmethod
	def Type(ent: TopoDS_Shape) -> Standard_Type: ...
	@staticmethod
	def TypeName(ent: TopoDS_Shape) -> str: ...

class TransferBRep_ShapeListBinder(Transfer_Binder):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, list: TopTools_HSequenceOfShape) -> None: ...
	def AddResult(self, res: TopoDS_Shape) -> None: ...
	def CompSolid(self, num: int) -> TopoDS_CompSolid: ...
	def Compound(self, num: int) -> TopoDS_Compound: ...
	def Edge(self, num: int) -> TopoDS_Edge: ...
	def Face(self, num: int) -> TopoDS_Face: ...
	def IsMultiple(self) -> bool: ...
	def NbShapes(self) -> int: ...
	def Result(self) -> TopTools_HSequenceOfShape: ...
	def ResultType(self) -> Standard_Type: ...
	def ResultTypeName(self) -> str: ...
	def SetResult(self, num: int, res: TopoDS_Shape) -> None: ...
	def Shape(self, num: int) -> TopoDS_Shape: ...
	def ShapeType(self, num: int) -> TopAbs_ShapeEnum: ...
	def Shell(self, num: int) -> TopoDS_Shell: ...
	def Solid(self, num: int) -> TopoDS_Solid: ...
	def Vertex(self, num: int) -> TopoDS_Vertex: ...
	def Wire(self, num: int) -> TopoDS_Wire: ...

class TransferBRep_ShapeMapper(Transfer_Finder):
	def __init__(self, akey: TopoDS_Shape) -> None: ...
	def Equates(self, other: Transfer_Finder) -> bool: ...
	def Value(self) -> TopoDS_Shape: ...
	def ValueType(self) -> Standard_Type: ...
	def ValueTypeName(self) -> str: ...

class TransferBRep_TransferResultInfo(Standard_Transient):
	def __init__(self) -> None: ...
	def Clear(self) -> None: ...
	def GetNoResult(self) -> int: ...
	def SetNoResult(self, value: int) -> None: ...
	def GetNoResultFail(self) -> int: ...
	def SetNoResultFail(self, value: int) -> None: ...
	def GetNoResultWarning(self) -> int: ...
	def SetNoResultWarning(self, value: int) -> None: ...
	def GetNoResultWarningFail(self) -> int: ...
	def SetNoResultWarningFail(self, value: int) -> None: ...
	def GetResult(self) -> int: ...
	def SetResult(self, value: int) -> None: ...
	def GetResultFail(self) -> int: ...
	def SetResultFail(self, value: int) -> None: ...
	def GetResultWarning(self) -> int: ...
	def SetResultWarning(self, value: int) -> None: ...
	def GetResultWarningFail(self) -> int: ...
	def SetResultWarningFail(self, value: int) -> None: ...

class TransferBRep_ShapeBinder(TransferBRep_BinderOfShape):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, res: TopoDS_Shape) -> None: ...
	def CompSolid(self) -> TopoDS_CompSolid: ...
	def Compound(self) -> TopoDS_Compound: ...
	def Edge(self) -> TopoDS_Edge: ...
	def Face(self) -> TopoDS_Face: ...
	def ShapeType(self) -> TopAbs_ShapeEnum: ...
	def Shell(self) -> TopoDS_Shell: ...
	def Solid(self) -> TopoDS_Solid: ...
	def Vertex(self) -> TopoDS_Vertex: ...
	def Wire(self) -> TopoDS_Wire: ...

# harray1 classes
# harray2 classes
# hsequence classes

class TransferBRep_HSequenceOfTransferResultInfo(TransferBRep_SequenceOfTransferResultInfo, Standard_Transient):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: TransferBRep_SequenceOfTransferResultInfo) -> None: ...
    def Sequence(self) -> TransferBRep_SequenceOfTransferResultInfo: ...
    def Append(self, theSequence: TransferBRep_SequenceOfTransferResultInfo) -> None: ...


transferbrep_CheckObject = transferbrep.CheckObject
transferbrep_Checked = transferbrep.Checked
transferbrep_CheckedShapes = transferbrep.CheckedShapes
transferbrep_PrintResultInfo = transferbrep.PrintResultInfo
transferbrep_ResultCheckList = transferbrep.ResultCheckList
transferbrep_ResultFromShape = transferbrep.ResultFromShape
transferbrep_SetShapeResult = transferbrep.SetShapeResult
transferbrep_SetTransientFromShape = transferbrep.SetTransientFromShape
transferbrep_ShapeMapper = transferbrep.ShapeMapper
transferbrep_ShapeResult = transferbrep.ShapeResult
transferbrep_ShapeResult = transferbrep.ShapeResult
transferbrep_ShapeState = transferbrep.ShapeState
transferbrep_Shapes = transferbrep.Shapes
transferbrep_Shapes = transferbrep.Shapes
transferbrep_TransferResultInfo = transferbrep.TransferResultInfo
transferbrep_TransferResultInfo = transferbrep.TransferResultInfo
transferbrep_TransientFromShape = transferbrep.TransientFromShape
TransferBRep_ShapeInfo_Type = TransferBRep_ShapeInfo.Type
TransferBRep_ShapeInfo_TypeName = TransferBRep_ShapeInfo.TypeName
