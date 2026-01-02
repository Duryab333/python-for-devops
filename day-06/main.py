from log_analyzer import LogAnalyzer


log_1 = LogAnalyzer("./app.log", "output.json")
log_count = log_1.analyzer()
log_1.write_json(log_count)
print(log_count)
