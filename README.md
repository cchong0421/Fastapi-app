# Python FastAPI Projects

## Requirement

- 安裝python 套件

  ```shell
  pip3 install -r requirements.txt
  ```

- 建立虛擬環境

  ```shell
  virtualenv fastapi-env
  or
  python -m venv fastapi-env
  source fastapi-env/bin/activate
  pip3 install -r requirements.txt
  ```

- 啟動虛擬環境和安裝相關 python 套件

  ```shell
  source fastapi-env/bin/activate
  pip3 install -r requirements.txt
  ```

- 關閉虛擬環境與刪除

  開啟終端機，然後執行 deativate 即可，完成後再將虛擬環境目錄刪除即可清除虛擬環境。

- add .env file

  ```shell
  SERVERNAME=<!-- YOUR_SERVER_NAME -->
  CERT_Password=<!-- YOUR_CERTIFICATE_PASSWORD-->
  MONGODBUSER=<!-- YOUR_MONGODB_USER_NAME -->
  MONGODBPWD=<!-- YOUR_MONGODB_USER_PASSWORD -->
  ```
  