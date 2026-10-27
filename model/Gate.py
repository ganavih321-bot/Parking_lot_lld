"""
package org.nailyourinterview.lld.parking_lot.model;

import lombok.AllArgsConstructor;
import lombok.Getter;
import org.nailyourinterview.lld.parking_lot.enums.GateType;

@Getter
@AllArgsConstructor
public abstract class Gate {
    protected final String id;

    public abstract GateType getType();
}
"""

"""
package org.nailyourinterview.lld.parking_lot.model;

import lombok.AllArgsConstructor;
import lombok.Getter;
import org.nailyourinterview.lld.parking_lot.enums.GateType;

@Getter
@AllArgsConstructor
public abstract class Gate {
    protected final String id;

    public abstract GateType getType();
}
"""

# from ..enums import GateType

# class Gate():
#     def __init__(self, id: str):
#         self.id = id

#     def getType(self) -> GateType:
#         raise NotImplementedError("Subclasses must implement getType() method")



from abc import ABC, abstractmethod
from enums.GateType import GateType


class Gate(ABC):
    def __init__(self, id: str):
        self.id = id

    def getId(self) -> str:
        return self.id

    @abstractmethod
    def getType(self) -> GateType:
        pass