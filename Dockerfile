# Copyright (c) 2019 Cisco and/or its affiliates.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM tiangolo/uwsgi-nginx-flask:python3.6

MAINTAINER Peter Mikus <peter.mikus@protonmail.ch>
LABEL Description="dash service image"
LABEL Version="0.1"

COPY ./requirements.txt /tmp
COPY ./app /app

RUN pip3 install -r /tmp/requirements.txt

ENV NGINX_WORKER_PROCESSES auto
ENV STATIC_PATH /app/static
