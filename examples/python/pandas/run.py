# This file is part of the Mantik Project.
# Copyright (c) 2020-2021 Mantik UG (Haftungsbeschränkt)
# Authors: See AUTHORS file
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License version 3.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.
#
# Additionally, the following linking exception is granted:
#
# If you modify this Program, or any covered work, by linking or
# combining it with other code, such other code is not for that reason
# alone subject to any of the requirements of the GNU Affero GPL
# version 3.
#
# You can be released from the requirements of the license by purchasing
# a commercial license.
#
"""Run sklearn.cluster.KMeans via mantik."""
import pathlib

import mantik

__file_loc__ = pathlib.Path(__file__).parent

with mantik.engine.Client("localhost", 8087) as client:
    dataset = client.add_artifact((__file_loc__ / "../sklearn").as_posix())
    pandas = client.add_artifact(__file_loc__.as_posix())

    simple_dataset = client.add_artifact(
        (__file_loc__ / "../sklearn/datasets/simple").as_posix(),
    )
    transform = client.add_artifact((__file_loc__ / "algorithms/transform").as_posix())
    transform2 = client.add_artifact((__file_loc__ / "algorithms/transform2").as_posix())

    with client.enter_session():
        result = client.apply([transform, transform2], data=simple_dataset)
        print(result.bundle.value)
