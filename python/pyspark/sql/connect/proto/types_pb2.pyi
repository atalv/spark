#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file

Licensed to the Apache Software Foundation (ASF) under one or more
contributor license agreements.  See the NOTICE file distributed with
this work for additional information regarding copyright ownership.
The ASF licenses this file to You under the Apache License, Version 2.0
(the "License"); you may not use this file except in compliance with
the License.  You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class DataType(google.protobuf.message.Message):
    """This message describes the logical [[DataType]] of something. It does not carry the value
    itself but only describes it.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class Boolean(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class Byte(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class Short(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class Integer(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class Long(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class Float(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class Double(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class String(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class Binary(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class NULL(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class Timestamp(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class Date(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class TimestampNTZ(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class CalendarInterval(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class YearMonthInterval(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        START_FIELD_FIELD_NUMBER: builtins.int
        END_FIELD_FIELD_NUMBER: builtins.int
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        start_field: builtins.int
        end_field: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            start_field: builtins.int | None = ...,
            end_field: builtins.int | None = ...,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions.Literal[
                "_end_field",
                b"_end_field",
                "_start_field",
                b"_start_field",
                "end_field",
                b"end_field",
                "start_field",
                b"start_field",
            ],
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "_end_field",
                b"_end_field",
                "_start_field",
                b"_start_field",
                "end_field",
                b"end_field",
                "start_field",
                b"start_field",
                "type_variation_reference",
                b"type_variation_reference",
            ],
        ) -> None: ...
        @typing.overload
        def WhichOneof(
            self, oneof_group: typing_extensions.Literal["_end_field", b"_end_field"]
        ) -> typing_extensions.Literal["end_field"] | None: ...
        @typing.overload
        def WhichOneof(
            self, oneof_group: typing_extensions.Literal["_start_field", b"_start_field"]
        ) -> typing_extensions.Literal["start_field"] | None: ...

    class DayTimeInterval(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        START_FIELD_FIELD_NUMBER: builtins.int
        END_FIELD_FIELD_NUMBER: builtins.int
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        start_field: builtins.int
        end_field: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            start_field: builtins.int | None = ...,
            end_field: builtins.int | None = ...,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions.Literal[
                "_end_field",
                b"_end_field",
                "_start_field",
                b"_start_field",
                "end_field",
                b"end_field",
                "start_field",
                b"start_field",
            ],
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "_end_field",
                b"_end_field",
                "_start_field",
                b"_start_field",
                "end_field",
                b"end_field",
                "start_field",
                b"start_field",
                "type_variation_reference",
                b"type_variation_reference",
            ],
        ) -> None: ...
        @typing.overload
        def WhichOneof(
            self, oneof_group: typing_extensions.Literal["_end_field", b"_end_field"]
        ) -> typing_extensions.Literal["end_field"] | None: ...
        @typing.overload
        def WhichOneof(
            self, oneof_group: typing_extensions.Literal["_start_field", b"_start_field"]
        ) -> typing_extensions.Literal["start_field"] | None: ...

    class UUID(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class Char(google.protobuf.message.Message):
        """Start compound types."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        LENGTH_FIELD_NUMBER: builtins.int
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        length: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            length: builtins.int = ...,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "length", b"length", "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class VarChar(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        LENGTH_FIELD_NUMBER: builtins.int
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        length: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            length: builtins.int = ...,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "length", b"length", "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class FixedBinary(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        LENGTH_FIELD_NUMBER: builtins.int
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        length: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            length: builtins.int = ...,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "length", b"length", "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class Decimal(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        SCALE_FIELD_NUMBER: builtins.int
        PRECISION_FIELD_NUMBER: builtins.int
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        scale: builtins.int
        precision: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            scale: builtins.int | None = ...,
            precision: builtins.int | None = ...,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions.Literal[
                "_precision",
                b"_precision",
                "_scale",
                b"_scale",
                "precision",
                b"precision",
                "scale",
                b"scale",
            ],
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "_precision",
                b"_precision",
                "_scale",
                b"_scale",
                "precision",
                b"precision",
                "scale",
                b"scale",
                "type_variation_reference",
                b"type_variation_reference",
            ],
        ) -> None: ...
        @typing.overload
        def WhichOneof(
            self, oneof_group: typing_extensions.Literal["_precision", b"_precision"]
        ) -> typing_extensions.Literal["precision"] | None: ...
        @typing.overload
        def WhichOneof(
            self, oneof_group: typing_extensions.Literal["_scale", b"_scale"]
        ) -> typing_extensions.Literal["scale"] | None: ...

    class StructField(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        class MetadataEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: builtins.str
            value: builtins.str
            def __init__(
                self,
                *,
                key: builtins.str = ...,
                value: builtins.str = ...,
            ) -> None: ...
            def ClearField(
                self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]
            ) -> None: ...

        NAME_FIELD_NUMBER: builtins.int
        DATA_TYPE_FIELD_NUMBER: builtins.int
        NULLABLE_FIELD_NUMBER: builtins.int
        METADATA_FIELD_NUMBER: builtins.int
        name: builtins.str
        @property
        def data_type(self) -> global___DataType: ...
        nullable: builtins.bool
        @property
        def metadata(
            self,
        ) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
        def __init__(
            self,
            *,
            name: builtins.str = ...,
            data_type: global___DataType | None = ...,
            nullable: builtins.bool = ...,
            metadata: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        ) -> None: ...
        def HasField(
            self, field_name: typing_extensions.Literal["data_type", b"data_type"]
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "data_type",
                b"data_type",
                "metadata",
                b"metadata",
                "name",
                b"name",
                "nullable",
                b"nullable",
            ],
        ) -> None: ...

    class Struct(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        FIELDS_FIELD_NUMBER: builtins.int
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        @property
        def fields(
            self,
        ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
            global___DataType.StructField
        ]: ...
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            fields: collections.abc.Iterable[global___DataType.StructField] | None = ...,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "fields", b"fields", "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class Array(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        ELEMENT_TYPE_FIELD_NUMBER: builtins.int
        CONTAINS_NULL_FIELD_NUMBER: builtins.int
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        @property
        def element_type(self) -> global___DataType: ...
        contains_null: builtins.bool
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            element_type: global___DataType | None = ...,
            contains_null: builtins.bool = ...,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def HasField(
            self, field_name: typing_extensions.Literal["element_type", b"element_type"]
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "contains_null",
                b"contains_null",
                "element_type",
                b"element_type",
                "type_variation_reference",
                b"type_variation_reference",
            ],
        ) -> None: ...

    class Map(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_TYPE_FIELD_NUMBER: builtins.int
        VALUE_TYPE_FIELD_NUMBER: builtins.int
        VALUE_CONTAINS_NULL_FIELD_NUMBER: builtins.int
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        @property
        def key_type(self) -> global___DataType: ...
        @property
        def value_type(self) -> global___DataType: ...
        value_contains_null: builtins.bool
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            key_type: global___DataType | None = ...,
            value_type: global___DataType | None = ...,
            value_contains_null: builtins.bool = ...,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions.Literal[
                "key_type", b"key_type", "value_type", b"value_type"
            ],
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "key_type",
                b"key_type",
                "type_variation_reference",
                b"type_variation_reference",
                "value_contains_null",
                b"value_contains_null",
                "value_type",
                b"value_type",
            ],
        ) -> None: ...

    NULL_FIELD_NUMBER: builtins.int
    BINARY_FIELD_NUMBER: builtins.int
    BOOLEAN_FIELD_NUMBER: builtins.int
    BYTE_FIELD_NUMBER: builtins.int
    SHORT_FIELD_NUMBER: builtins.int
    INTEGER_FIELD_NUMBER: builtins.int
    LONG_FIELD_NUMBER: builtins.int
    FLOAT_FIELD_NUMBER: builtins.int
    DOUBLE_FIELD_NUMBER: builtins.int
    DECIMAL_FIELD_NUMBER: builtins.int
    STRING_FIELD_NUMBER: builtins.int
    CHAR_FIELD_NUMBER: builtins.int
    VAR_CHAR_FIELD_NUMBER: builtins.int
    DATE_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    TIMESTAMP_NTZ_FIELD_NUMBER: builtins.int
    CALENDAR_INTERVAL_FIELD_NUMBER: builtins.int
    YEAR_MONTH_INTERVAL_FIELD_NUMBER: builtins.int
    DAY_TIME_INTERVAL_FIELD_NUMBER: builtins.int
    ARRAY_FIELD_NUMBER: builtins.int
    STRUCT_FIELD_NUMBER: builtins.int
    MAP_FIELD_NUMBER: builtins.int
    UUID_FIELD_NUMBER: builtins.int
    FIXED_BINARY_FIELD_NUMBER: builtins.int
    USER_DEFINED_TYPE_REFERENCE_FIELD_NUMBER: builtins.int
    @property
    def null(self) -> global___DataType.NULL: ...
    @property
    def binary(self) -> global___DataType.Binary: ...
    @property
    def boolean(self) -> global___DataType.Boolean: ...
    @property
    def byte(self) -> global___DataType.Byte:
        """Numeric types"""
    @property
    def short(self) -> global___DataType.Short: ...
    @property
    def integer(self) -> global___DataType.Integer: ...
    @property
    def long(self) -> global___DataType.Long: ...
    @property
    def float(self) -> global___DataType.Float: ...
    @property
    def double(self) -> global___DataType.Double: ...
    @property
    def decimal(self) -> global___DataType.Decimal: ...
    @property
    def string(self) -> global___DataType.String:
        """String types"""
    @property
    def char(self) -> global___DataType.Char: ...
    @property
    def var_char(self) -> global___DataType.VarChar: ...
    @property
    def date(self) -> global___DataType.Date:
        """Datatime types"""
    @property
    def timestamp(self) -> global___DataType.Timestamp: ...
    @property
    def timestamp_ntz(self) -> global___DataType.TimestampNTZ: ...
    @property
    def calendar_interval(self) -> global___DataType.CalendarInterval:
        """Interval types"""
    @property
    def year_month_interval(self) -> global___DataType.YearMonthInterval: ...
    @property
    def day_time_interval(self) -> global___DataType.DayTimeInterval: ...
    @property
    def array(self) -> global___DataType.Array:
        """Complex types"""
    @property
    def struct(self) -> global___DataType.Struct: ...
    @property
    def map(self) -> global___DataType.Map: ...
    @property
    def uuid(self) -> global___DataType.UUID: ...
    @property
    def fixed_binary(self) -> global___DataType.FixedBinary: ...
    user_defined_type_reference: builtins.int
    def __init__(
        self,
        *,
        null: global___DataType.NULL | None = ...,
        binary: global___DataType.Binary | None = ...,
        boolean: global___DataType.Boolean | None = ...,
        byte: global___DataType.Byte | None = ...,
        short: global___DataType.Short | None = ...,
        integer: global___DataType.Integer | None = ...,
        long: global___DataType.Long | None = ...,
        float: global___DataType.Float | None = ...,
        double: global___DataType.Double | None = ...,
        decimal: global___DataType.Decimal | None = ...,
        string: global___DataType.String | None = ...,
        char: global___DataType.Char | None = ...,
        var_char: global___DataType.VarChar | None = ...,
        date: global___DataType.Date | None = ...,
        timestamp: global___DataType.Timestamp | None = ...,
        timestamp_ntz: global___DataType.TimestampNTZ | None = ...,
        calendar_interval: global___DataType.CalendarInterval | None = ...,
        year_month_interval: global___DataType.YearMonthInterval | None = ...,
        day_time_interval: global___DataType.DayTimeInterval | None = ...,
        array: global___DataType.Array | None = ...,
        struct: global___DataType.Struct | None = ...,
        map: global___DataType.Map | None = ...,
        uuid: global___DataType.UUID | None = ...,
        fixed_binary: global___DataType.FixedBinary | None = ...,
        user_defined_type_reference: builtins.int = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "array",
            b"array",
            "binary",
            b"binary",
            "boolean",
            b"boolean",
            "byte",
            b"byte",
            "calendar_interval",
            b"calendar_interval",
            "char",
            b"char",
            "date",
            b"date",
            "day_time_interval",
            b"day_time_interval",
            "decimal",
            b"decimal",
            "double",
            b"double",
            "fixed_binary",
            b"fixed_binary",
            "float",
            b"float",
            "integer",
            b"integer",
            "kind",
            b"kind",
            "long",
            b"long",
            "map",
            b"map",
            "null",
            b"null",
            "short",
            b"short",
            "string",
            b"string",
            "struct",
            b"struct",
            "timestamp",
            b"timestamp",
            "timestamp_ntz",
            b"timestamp_ntz",
            "user_defined_type_reference",
            b"user_defined_type_reference",
            "uuid",
            b"uuid",
            "var_char",
            b"var_char",
            "year_month_interval",
            b"year_month_interval",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "array",
            b"array",
            "binary",
            b"binary",
            "boolean",
            b"boolean",
            "byte",
            b"byte",
            "calendar_interval",
            b"calendar_interval",
            "char",
            b"char",
            "date",
            b"date",
            "day_time_interval",
            b"day_time_interval",
            "decimal",
            b"decimal",
            "double",
            b"double",
            "fixed_binary",
            b"fixed_binary",
            "float",
            b"float",
            "integer",
            b"integer",
            "kind",
            b"kind",
            "long",
            b"long",
            "map",
            b"map",
            "null",
            b"null",
            "short",
            b"short",
            "string",
            b"string",
            "struct",
            b"struct",
            "timestamp",
            b"timestamp",
            "timestamp_ntz",
            b"timestamp_ntz",
            "user_defined_type_reference",
            b"user_defined_type_reference",
            "uuid",
            b"uuid",
            "var_char",
            b"var_char",
            "year_month_interval",
            b"year_month_interval",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["kind", b"kind"]
    ) -> typing_extensions.Literal[
        "null",
        "binary",
        "boolean",
        "byte",
        "short",
        "integer",
        "long",
        "float",
        "double",
        "decimal",
        "string",
        "char",
        "var_char",
        "date",
        "timestamp",
        "timestamp_ntz",
        "calendar_interval",
        "year_month_interval",
        "day_time_interval",
        "array",
        "struct",
        "map",
        "uuid",
        "fixed_binary",
        "user_defined_type_reference",
    ] | None: ...

global___DataType = DataType
