import React, { useCallback, useState } from 'react';
import { LeftOutlined} from '@ant-design/icons';
import { SvgMenu } from '../../components/Icons';
import { useNavigate } from "react-router-dom";
import { InfoCircleOutlined } from '@ant-design/icons';
import { Button, Form, Input, Radio, Tag } from 'antd';
import './researchpage.css';



const InnerResearch = ({setPage, page, band, setBand}) => {
    const navigate = useNavigate();
    const [form] = Form.useForm();
    const [requiredMark, setRequiredMarkType] = useState('optional');

    return(
        <>
        <h1 className="h1">Информация про сотрудника</h1>
        <div className="inner">
            <div className="tools">
            <div className="tilte">
                <button onClick={() => navigate('/userpage')}>
                 <LeftOutlined />
                </button>
                <div className="spin"></div>
                <h2>Сотрудник</h2>
            </div>
          </div>
          <Form
      form={form}
      layout="vertical"
      initialValues={{ requiredMarkValue: requiredMark }}
    >
      {/*<Form.Item label="Required Mark" name="requiredMarkValue">
         <Radio.Group>
          <Radio.Button value>Default</Radio.Button>
          <Radio.Button value="optional">Optional</Radio.Button>
          <Radio.Button value={false}>Hidden</Radio.Button>
          <Radio.Button value="customize">Customize</Radio.Button>
        </Radio.Group>
      </Form.Item> */}
   
      <Form.Item
        label="ФИО"
        tooltip={{ title: 'Tooltip with customize icon', icon: <InfoCircleOutlined /> }}
      >
        <Input placeholder="input placeholder" />
      </Form.Item>

      <Form.Item
        label="Email"
        tooltip={{ title: 'Tooltip with customize icon', icon: <InfoCircleOutlined /> }}
      >
        <Input placeholder="input placeholder" />
      </Form.Item>

      <Form.Item
        label="Должность"
        tooltip={{ title: 'Tooltip with customize icon', icon: <InfoCircleOutlined /> }}
      >
        <Input placeholder="input placeholder" />
      </Form.Item>

      <Form.Item
        label="Отдел"
        tooltip={{ title: 'Tooltip with customize icon', icon: <InfoCircleOutlined /> }}
      >
        <Input placeholder="input placeholder" />
      </Form.Item>

      <Form.Item
        label="Проживание"
        tooltip={{ title: 'Tooltip with customize icon', icon: <InfoCircleOutlined /> }}
      >
        <Input placeholder="input placeholder" />
      </Form.Item>

      <div className="tilte">
                <div className="spin"></div>
                <h2>Дополнитлеьные данные</h2>
        </div>


      <Form.Item>
        <Button type="btn-blue"
        onClick={setBand}
        >Добавить</Button>
      </Form.Item>
    </Form>
        </div>
        </>
    )
}

export default InnerResearch;