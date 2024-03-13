{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "## 1. Numpy\n",
        "- 파이썬에서 수학적인 계산(행렬, 벡터, 차원)을 편하게 할 수 있도록 돕는 라이브러리"
      ],
      "metadata": {
        "id": "i-KDV36uSVh5"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "%pip install numpy"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1cbsN3o0Sdul",
        "outputId": "b3ed9baa-a418-4d25-f859-546aca3bdf13"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: numpy in /usr/local/lib/python3.10/dist-packages (1.25.2)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np"
      ],
      "metadata": {
        "id": "zhfNhIFeSijS"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 1차원 배열\n",
        "arr1 = np.array([1,2,3])\n",
        "\n",
        "arr1\n",
        "type(arr1)\n",
        "arr1.shape # 1행 3열\n",
        "arr1.ndim # 1차원"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "arM1cZw5S4h6",
        "outputId": "e4371d85-0ccf-4bb2-bc14-fe1829a5878a"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1"
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 2차원 배열\n",
        "arr2 = np.array([[1,2,3], [1,2,3]])\n",
        "\n",
        "arr2\n",
        "type(arr2)\n",
        "arr2.shape # 2행 3열의 행렬\n",
        "arr2.ndim # 2차원"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Dr-4HlzyS_1R",
        "outputId": "14290041-58fd-4460-e33f-c4385ca28c17"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "2"
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# ndarray 데이터 타입\n",
        "\n",
        "arr3 = ['1', '2', '3']\n",
        "\n",
        "arr3 = np.array(arr3)\n",
        "arr3 = arr3.astype(np.int64)\n",
        "arr3.dtype"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xFuhZ0AmTRgv",
        "outputId": "0ee1ae13-83e3-4207-b25b-248937ffb278"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "dtype('int64')"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# ndarray 생성\n",
        "arr = np.arange(10)\n",
        "\n",
        "arr > 5 # boolean indexing\n",
        "# arr[arr > 5]\n",
        "\n",
        "arr[[False, False, False, False, False, False,  True,  True,  True, True]]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hKpd0atfTw4S",
        "outputId": "89ee7f6f-2d34-499f-e388-5c5e0389c2fe"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([6, 7, 8, 9])"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "np.zeros((3,2))\n",
        "np.ones((3,2))\n",
        "np.ones((10,10))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zg2RDCr8UI1A",
        "outputId": "e18e3a21-d2a6-4a49-cd29-75ebd6071dc4"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],\n",
              "       [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],\n",
              "       [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],\n",
              "       [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],\n",
              "       [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],\n",
              "       [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],\n",
              "       [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],\n",
              "       [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],\n",
              "       [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],\n",
              "       [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]])"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# reshape => 차원을 변경\n",
        "arr = np.arange(10)\n",
        "\n",
        "arr.reshape(2,5)\n",
        "arr.reshape(5,2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZcoLi-QlUeoB",
        "outputId": "4159307f-ed6c-40bc-cc2c-82e9cc6eb249"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[0, 1],\n",
              "       [2, 3],\n",
              "       [4, 5],\n",
              "       [6, 7],\n",
              "       [8, 9]])"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# indexing & slicing\n",
        "arr[0]\n",
        "arr[5:]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8skTJ3TfU5J6",
        "outputId": "98f208a4-3fc6-4373-812e-9da665021a30"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([5, 6, 7, 8, 9])"
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Q1. 2차원 배열에서 행렬의 각 행의 평균을 계산하는 코드를 작성하세요.\n",
        "# np.mean()\n",
        "\n",
        "arr = np.array([[1,2,3], [4,5,6], [7,8,9]])\n",
        "\n",
        "arr.shape\n",
        "\n",
        "print(arr)\n",
        "# axis=0(열), axis=1(행), axis=2(채널)\n",
        "np.mean(arr, axis=1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MZtn40jbVJVO",
        "outputId": "583966a2-84b6-45da-969a-7085722e2a59"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[1 2 3]\n",
            " [4 5 6]\n",
            " [7 8 9]]\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([2., 5., 8.])"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Q2. 1차원 배열에서 짝수 인덱스의 값을 출력하는 코드를 작성하세요.\n",
        "arr = np.array([1, 2, 3, 4, 5, 6])\n",
        "\n",
        "even_indexes = np.arange(0, arr.size, 2)\n",
        "\n",
        "print(arr[even_indexes])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "F6_hoxIlV4jK",
        "outputId": "0f7c2fe6-0c15-4d76-90b1-85403f8ea4cb"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1 3 5]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Q3. 2차원 배열의 주 대각선 상에 있는 원소들을 출력하는 코드를 작성하세요.\n",
        "\n",
        "arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])\n",
        "arr.shape\n",
        "\n",
        "# diag\n",
        "np.diag(arr)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1SsIEIcJWxif",
        "outputId": "cc142d8b-8695-47ad-902d-a119396f91bf"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([1, 5, 9])"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Q4. 2차원 배열에서 각 열의 표준 편차를 계산하는 코드를 작성하세요.\n",
        "# 표준 편차 => np.std()\n",
        "\n",
        "arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])\n",
        "\n",
        "np.std(arr)\n",
        "\n",
        "print(arr)\n",
        "\n",
        "np.std(arr, axis=0)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5JvFkwNHXDt2",
        "outputId": "2fd2c965-5524-43d3-e9b4-60adf38fd2a3"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[1 2 3]\n",
            " [4 5 6]\n",
            " [7 8 9]]\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([2.44948974, 2.44948974, 2.44948974])"
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Q5. 1차원 배열에서 중앙값(median)을 계산하는 코드를 작성하세요.\n",
        "\n",
        "arr = np.array([1, 2, 3, 4, 5])\n",
        "np.median(arr)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xHbSufXmYCWx",
        "outputId": "e632f1a2-8f0d-42de-a5b0-9b26b9173e68"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "3.0"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Q6. 1차원 배열에서 원소의 값이 5 이상인 것들만 출력하는 코드를 작성하세요.\n",
        "# - boolean indexing\n",
        "\n",
        "arr = np.array([1, 4, 6, 3, 9, 2, 7, 8])\n",
        "\n",
        "arr[arr >= 5]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Q6QJij2aYc7J",
        "outputId": "ab72135e-4954-4763-83be-659e118ee8a2"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([6, 9, 7, 8])"
            ]
          },
          "metadata": {},
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Q7. 1차원 배열에서 원소의 값이 3 또는 5인 것들의 인덱스를 출력하는 코드를 작성하세요.\n",
        "\n",
        "arr = np.array([1, 3, 5, 2, 4, 6, 3, 5, 7])\n",
        "\n",
        "np.where((arr == 3) | (arr == 5)) # and&, or|"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GwJJuT85YhJl",
        "outputId": "e9d020b5-9288-489a-d683-35404c1e917d"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(array([1, 2, 6, 7]),)"
            ]
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "https://github.com/scikit-learn/scikit-learn/blob/9aaed498795f68e5956ea762fef9c440ca9eb239/sklearn/gaussian_process/kernels.py"
      ],
      "metadata": {
        "id": "aAPOJeJHZJso"
      }
    }
  ]
}