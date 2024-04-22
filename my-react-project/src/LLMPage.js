import React, { useState } from 'react';
import styles from './LLMPage.module.css';

function LLMPage() {
  const [inputText, setInputText] = useState('');
  const [receivedText, setReceivedText] = useState('');
  const [loading, setLoading] = useState(false); // 新增loading状态用于控制进度条显示

  const handleInputChange = (event) => {
    setInputText(event.target.value);
  };

  const handleSendClick = async () => {
    setLoading(true); // 发送请求前显示进度条
    try {
      const requestData = {
        'input_string': inputText
      };
      console.log("Sending data to LLM:", requestData); // 打印发送到LLM的数据到控制台
      const response = await fetch('http://127.0.0.1:5000/LLM', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestData)
      });

      if (response.ok) {
        const responseData = await response.json();
        console.log("Received data from LLM:", responseData); // 打印接收到的数据到控制台
        const result = responseData.result;
        setReceivedText(result);
        setInputText('');
      } else {
        throw new Error('Failed to send text to LLM.');
      }
    } catch (error) {
      console.error('Error sending text to LLM:', error);
      alert('Error sending text to LLM: ' + error.message);
    } finally {
      setLoading(false); // 请求完成后隐藏进度条
    }
  };

  return (
    <div className={styles.container}>
      <h1 className={styles.title}>文心一言</h1>
      <div className={styles.chatBox}>
        <div className={styles.inputContainer}>
          <input
            type="text"
            value={inputText}
            onChange={handleInputChange}
            placeholder="输入您的消息..."
            className={styles.input}
          />
          <button onClick={handleSendClick} className={styles.sendButton}>发送</button>
        </div>
        {loading && <div className={styles.loader}></div>} {/* 根据loading状态显示/隐藏进度条 */}
        <div className={styles.receivedText}>{receivedText}</div>
      </div>
    </div>
  );
}

export default LLMPage;
