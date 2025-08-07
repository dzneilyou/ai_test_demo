package com.example.springaitest;

import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.client.advisor.MessageChatMemoryAdvisor;
import org.springframework.ai.chat.client.advisor.SimpleLoggerAdvisor;
import org.springframework.ai.content.Media;
import org.springframework.core.io.ClassPathResource;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;

/**
 * Spring AI控制器 - 1.0.0版本
 *
 * @author neilyou
 * @version 1.0
 */
@RestController
public class AiController {

    private final ChatClient chatClient;



    public AiController(ChatClient.Builder chatClientBuilder) {
        this.chatClient = chatClientBuilder.build();
    }


//    @GetMapping("/ai/chat")
//    public String chat(@RequestParam(name = "userInput", defaultValue = "你好，请介绍一下Spring AI") String userInput) {
//        try {
//            // 使用Spring AI 1.0.0的流式API
//            return this.chatClient.prompt()
//                    .user(userInput)
//                    .call()
//                    .content();
//        } catch (Exception e) {
//            return "抱歉，AI服务暂时不可用: " + e.getMessage();
//        }
//    }

    @PostMapping("/ai/chat")
    public String chatPost(@RequestParam(name = "userInput", defaultValue = "你好，请介绍一下Spring AI") String userInput) {
        try {
            // 使用Spring AI 1.0.0的流式API
            return this.chatClient.prompt()
                    .user(userInput)
                    .advisors(
                            new SimpleLoggerAdvisor()
//                            ,new MessageChatMemoryAdvisor()
                    )
                    .call()
                    .content();

        } catch (Exception e) {
            return "抱歉，AI服务暂时不可用: " + e.getMessage();
        }
    }






    @GetMapping("/ai/chat/media")
    public String chatPostWithMedia(@RequestParam(name = "userInput", defaultValue = "你好，请介绍一下Spring AI") String userInput) {
        try {
            return chatClient
                    .prompt()
                    .user(u -> u.text(
                                    "You are a very professional document summarization specialist. Please summarize the given document.")
                            .media(Media.Format.DOC_PDF, new ClassPathResource("/spring-ai-reference-overview.pdf")))
                    .call()
                    .content();

        } catch (Exception e) {
            return "抱歉，AI服务暂时不可用: " + e.getMessage();
        }
    }



    /**
     * 流式聊天接口
     *
     * @param userInput 用户输入
     * @return 流式响应
     */
    @GetMapping(value = "/ai/stream", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
    public Flux<String> streamChat(@RequestParam(name = "userInput", defaultValue = "你好，请介绍一下Spring AI") String userInput) {
        try {
            // 使用Spring AI 1.0.0的流式API
            return this.chatClient.prompt()
                    .user(userInput)
                    .advisors(new SimpleLoggerAdvisor())
                    .stream()
                    .content();
        } catch (Exception e) {
            return Flux.just("抱歉，AI服务暂时不可用: " + e.getMessage());
        }




    }

    /**
     * 健康检查接口
     *
     * @return 服务状态
     */
    @GetMapping("/ai/health")
    public String health() {
        return "Spring AI 1.0.0服务运行正常！";
    }

    @GetMapping("/ai/debug")
    public String debug() {
        StringBuilder sb = new StringBuilder();
        sb.append("调试信息：\n");
        sb.append("- ChatClient注入状态: ").append(chatClient != null ? "成功" : "失败").append("\n");
        sb.append("- ChatClient类型: ").append(chatClient != null ? chatClient.getClass().getName() : "null").append("\n");
        sb.append("- Spring AI版本: 1.0.0\n");
        sb.append("- 当前时间: ").append(System.currentTimeMillis()).append("\n");
        sb.append("- 状态: 应用启动成功，ChatClient已配置");
        return sb.toString();
    }

    /**
     * 项目信息接口
     *
     * @return 项目信息
     */
    @GetMapping("/ai/info")
    public String info() {
        return """
                Spring AI项目信息：
                - 项目名称: spring-aitest
                - Spring Boot版本: 3.5.4
                - Spring AI版本: 1.0.0 (正式版)
                - Java版本: 17
                - 状态: 运行正常
                - API: 使用Spring AI 1.0.0新API
                - 依赖: spring-ai-client-chat
                - 文档: 参考Spring AI官方文档
                - ChatClient: 已配置并注入成功
                """;
    }

    /**
     * 版本对比接口
     *
     * @return 版本对比信息
     */
    @GetMapping("/ai/version-comparison")
    public String versionComparison() {
        return """
                Spring AI版本对比：

                🔄 1.0.0-M6 (里程碑版本):
                - 包名: org.springframework.ai.chat.ChatClient
                - API: chatClient.call(prompt)
                - 返回: ChatResponse
                - 特点: 开发阶段，API简单直接

                🚀 1.0.0 (正式版本):
                - 包名: org.springframework.ai.chat.client.ChatClient
                - API: chatClient.prompt().user(message).call().content()
                - 返回: CallResponseSpec
                - 特点: 流式API，链式调用
                - 依赖: spring-ai-client-chat

                📝 主要变化：
                1. 流式API设计
                2. Builder模式
                3. 链式调用
                4. 模块化依赖
                5. 更好的性能

                💡 官方文档示例：
                ```java
                return this.chatClient.prompt()
                    .user(userInput)
                    .call()
                    .content();
                ```
                """;
    }

    /**
     * API使用指南
     *
     * @return API使用指南
     */
    @GetMapping("/ai/api-guide")
    public String apiGuide() {
        return """
                Spring AI 1.0.0 API使用指南：

                ✅ 当前实现：
                - 使用官方推荐的流式API
                - chatClient.prompt().user(message).call().content()
                - 参考Spring AI官方文档

                📚 官方文档要点：
                1. ChatClient使用Builder模式
                2. 支持流式API和同步编程模型
                3. 使用链式调用构建Prompt
                4. call()方法发送请求到AI模型
                5. content()方法返回String响应

                🔗 相关资源：
                - Spring AI官方文档: https://docs.spring.io/spring-ai/reference/api/chatclient.html
                - Spring AI GitHub仓库
                - Spring AI示例项目

                🛠️ 下一步：
                1. 配置AI模型（OpenAI等）
                2. 添加系统提示词
                3. 实现聊天记忆功能
                4. 添加向量数据库支持
                """;
    }
} 