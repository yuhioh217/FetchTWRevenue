from src.getRevenue import getRevenue

if __name__ == "__main__":
  _revenue = getRevenue('1','2018', '11')
  totalPage = _revenue.getPageCount()
  for i in range(1, totalPage + 1):
    _revenue.setPage(str(i))
    _revenue.fetchHtml()
    _revenue.dataprocessing()
  
  allData = _revenue.getDataArr()
  for data in allData:
    print(data[1], data[2], data[3], data[4], data[5], data[6])
