# Copyright (c) 2013 Amazon.com, Inc. or its affiliates.  All Rights Reserved
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
from tests.unit import unittest
from tests.unit import AWSMockServiceTestCase

from boto.s3.connection import S3Connection


class TestSignatureAlteration(AWSMockServiceTestCase):
    connection_class = S3Connection

    def test_unchanged(self):
        self.assertEqual(
            self.service_connection._required_auth_capability(),
            ['s3']
        )

    def test_switched(self):
        conn = self.connection_class(
            aws_access_key_id='less',
            aws_secret_access_key='more',
            host='s3.cn-north-1.amazonaws.com.cn'
        )
        self.assertEqual(
            conn._required_auth_capability(),
            ['hmac-v4-s3']
        )


if __name__ == "__main__":
    unittest.main()
