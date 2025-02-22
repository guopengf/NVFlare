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

from nvflare.apis.fl_context import FLContext
from nvflare.app_common.psi.dh_psi.dh_psi_workflow import DhPSIWorkFlow
from nvflare.app_common.psi.psi_workflow_spec import PSIWorkflow
from nvflare.app_common.workflows.psi_controller import PSIController


class DhPSIController(PSIController):
    def __init__(self):
        super().__init__("")

    def load_psi_workflow(self, fl_ctx: FLContext, psi_workflow_id: str) -> PSIWorkflow:
        psi_workflow = DhPSIWorkFlow()
        psi_workflow.initialize(fl_ctx, controller=self)
        return psi_workflow
