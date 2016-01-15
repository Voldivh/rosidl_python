# Copyright 2016 Open Source Robotics Foundation, Inc.
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

from nose.tools import assert_raises

from rosidl_generator_py.msg import Bool
from rosidl_generator_py.msg import Constants
from rosidl_generator_py.msg import Empty
from rosidl_generator_py.msg import Float32
from rosidl_generator_py.msg import Float64
from rosidl_generator_py.msg import Int32
from rosidl_generator_py.msg import Int64
from rosidl_generator_py.msg import Strings


def test_strings():
    a = Strings()

    assert(a.empty_string is None)
    assert(a.def_string == "Hello world!")


def test_invalid_attribute():
    a = Strings()

    assert_raises(AttributeError, setattr, a, "invalid_string1", "foo")

    assert_raises(AttributeError, getattr, a, "invalid_string2")


def test_constructor():
    a = Strings(empty_string="foo")

    assert(a.empty_string == "foo")

    assert_raises(AssertionError, Strings, unknown_field="test")


def test_constants():
    assert(Constants.X == 123)
    assert(Constants.Y == -123)
    assert(Constants.FOO == "foo")

    assert_raises(AttributeError, setattr, Constants, "FOO", "bar")