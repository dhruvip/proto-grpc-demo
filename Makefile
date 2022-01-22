.PHONY: build
build:
	docker build -t proto-demo .

.PHONY: proto
proto:
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. hello.proto