#!/bin/bash

# Copyright (c) 2025 Huawei Device Co., Ltd.
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

set -e
cd $1

_all_patches=(
  "0001-musl-build-fix.patch"
)
for filename in "${_all_patches[@]}"
  do
    echo "Applying patch ${filename}..."
    if patch --dry-run -p1 < ${filename} > /dev/null 2>&1
      then
        echo "Verify patch ${filename} ok. start apply."
        patch -p1 < ${filename} --fuzz=0 --no-backup-if-mismatch
    else
      echo "Verify patch ${filename} not ok. patch already apply? skip apply."
    fi
  done
exit 0
