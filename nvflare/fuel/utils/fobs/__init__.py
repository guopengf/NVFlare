# Copyright (c) 2021-2022, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from nvflare.fuel.utils.fobs.decomposer import Decomposer
from nvflare.fuel.utils.fobs.fobs import (
    auto_register_enum_types,
    deserialize,
    deserialize_stream,
    num_decomposers,
    register,
    register_data_classes,
    register_enum_types,
    register_folder,
    reset,
    serialize,
    serialize_stream,
)

# aliases for compatibility to Pickle/json
load = deserialize_stream
loads = deserialize
dump = serialize_stream
dumps = serialize
