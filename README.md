# lambda-debug-logging

lambda-debug-logging is a Python library that helps reduce logging costs without sacrificing debugging capabilities.  The library will automatically detect when your Lambda execution as failed.  If the execution failed, then all of your debug logs will get written out to CloudWatch.  If your execution succeeded, then only a small percentage of your debug logs will get written out to CloudWatch.

## Installation

```
$ pip install lambda-debug-logging
```

## Usage

```
from lambda_debug_logging import lambda_debug_logging

@lambda_debug_logging()
def handler(event, context):
    return "success!"
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

- [Basic Contributor Guide](CONTRIBUTING.md)
- [Development Guides](docs/devguide.md)

## License

[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0/)

## Dependencies

[Dependency Notices](NOTICE.md)