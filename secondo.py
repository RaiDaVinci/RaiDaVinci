import numpy as np

def main():
    mioArr0d=np.array(5)
    print(mioArr0d)
    print(mioArr0d.ndim)
    mioArr1d = np.array([1,2,3,4,5])
    print(mioArr1d)
    print(mioArr1d.ndim)
    mioArr2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    print(mioArr2d)
    print(mioArr2d.ndim)
    mioArr3d = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[1, 2, 3, 4, 5], [6, 7, 18, 9, 10]]])
    print(mioArr3d)
    print(mioArr3d.ndim)
    print(mioArr3d[1,1,4])


if __name__=="__main__":
    main()
