import pandas as pd

def read_url_from_csv(file_path):
    """
    从csv读url，拼接字段
    :param file_path:
    :param cols:
    :return:
    """
    data = read_data(file_path)
    return get_urls(data)


def read_data(file_path):
    data = pd.read_csv(file_path, sep='\t', error_bad_lines=False, header=None,
                       names=['index', 'path', 'unkonw',
                              'ip1', 'ip2', 'port1', 'port2',
                              'date', 'host', 'ua', 'method',
                              'status_code', 'len', 'deep_label',
                              'rule_label'])
    print("reading data:", file_path)
    print("Target len:", len(data))
    return data


def get_urls(dataFrame):
    dataFrame.request_text = dataFrame.apply(lambda x: "http://" + str(x.host) + str(x.path), axis=1)

    return list(dataFrame.request_text)


# data = read_url_from_csv("/Users/gavia/Downloads/流量工作文档/webshell类别/crawl_webshell_data/webshell_data/webshell_check/webshell_check_18_07_12/webshell_data0712.csv")
# print("totals url:", len(data))
# print(data[1000:1200])