# Description
This project used for auto-scale [provision resource](https://help.aliyun.com/document_detail/138103.html?spm=a2c4g.11186623.6.626.44864085lYFFpP) of [FunctionCompute FC](https://help.aliyun.com/product/50980.html?spm=a2c4g.11186623.6.540.22a34085vt6i7U). With [Serverless workflow](https://help.aliyun.com/knowledge_detail/114020.html?spm=5176.cnfnf.0.0.6ce91ea8KSYhc7) and 
[schedule](https://help.aliyun.com/document_detail/168926.html?spm=a2c4g.11186623.6.586.7fb73a65PfrKiS) you can set multi strategy for when and how to update provision resource. And all changes will record in 
Serverless workflow.

## Dependencies
- Install [Funcraft](https://github.com/alibaba/funcraft/blob/master/docs/specs/2018-04-03-zh-cn.md?spm=a2c4g.11186623.2.7.ynnKi4&file=2018-04-03-zh-cn.md) tool

## Usage
1. Run `fun deploy`
   Deploy FC function and Serverless workflow. This will create:
   - FC service: ProvisionAutoScaleService
   - FC function: main
   - Workflow: ProvisionAutoScaleFlow
   
2. Go [Serverless workflow Console](https://fnf.console.aliyun.com/) to create schedule for workflow, and set the payload as:
```json
{
     "serviceName": "YOUR_TARGET_SERVICE",
     "functionName": "YOUR_TARGET_FUNCTION",
     "alias": "YOUR_TARGET_ALIAS",
     "provisionCount": 10
}
```
You can create multi schedules as you want.
