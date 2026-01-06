import datetime
import logging
import os

from config import logs_path


class LogUtil:
    @staticmethod
    def generate_log_name():
        # 获取当前时间
        now = datetime.datetime.now()
        # 格式化时间为字符串，例如：2023-10-05_14-30-00
        log_name = now.strftime("%Y%m%d")
        return log_name

    @staticmethod
    def get_logger():
        # 生成日志名称
        log_name = LogUtil.generate_log_name()
        # 日志文件路径
        log_file_path = os.path.join(logs_path, f'{log_name}.log')

        # 确保日志目录存在
        os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

        # 配置日志记录器
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        # 创建文件处理器，将日志写入文件
        file_handler = logging.FileHandler(log_file_path,encoding='utf-8')
        file_handler.setLevel(logging.INFO)

        # 创建控制台处理器，将日志输出到控制台
        # console_handler = logging.StreamHandler()
        # console_handler.setLevel(logging.INFO)

        # 定义日志格式
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s'
        )
        file_handler.setFormatter(formatter)
        # console_handler.setFormatter(formatter)

        # 将处理器添加到日志记录器
        logger.addHandler(file_handler)
        # logger.addHandler(console_handler)

        return logger


# 使用示例
if __name__ == "__main__":
    logger = LogUtil.get_logger()
    logger.info("接口自动化测试开始")
    # 在这里添加你的接口自动化测试代码
    logger.info("接口自动化测试结束")
