# RemoveUnityFakeHeader
在Unity bundle包的標頭前塞入垃圾資料是一種常見的反拆包方式，這裡提供一個簡單的python腳本做為參考

Stuffing junk in front of the Unity bundle header is a common way to unpack. Here is a simple python script for reference. This script will remove junk before the UnityFS header of all Unity bundles in the specified directory and save it.

## Note
https://github.com/28598519a/RemoveUnityFakeHeader/blob/81dd0fffed8604a18e1c7f0c7300e29e08ddc1ca/RemoveUnityFakeHeader.py#L8
Unity bundle檔案的副檔名，如果沒副檔名，這行改一下把所有檔案全處理一遍一樣可行
