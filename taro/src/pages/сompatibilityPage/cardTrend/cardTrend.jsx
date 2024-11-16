import React from 'react';
import './cardtrend.css'; 
import {ArrowDownOutlined, ArrowUpOutlined} from '@ant-design/icons';

const TrendCard = ({data, trend}) => {

    return (
        <div className="trend-card">
            <div className="field">
            </div>
            <div>
                <imf src="./pyblic/convCard.svg"/>
                <div className="inn-card">
                    <span>Сейчас</span>
                    <span>{(data  ?? '-')+ '%'}</span>
                </div>
            </div>
            <div>
                {trend>=0 &&
                    <span className="green"><ArrowUpOutlined />{trend}</span>}
                {trend <0 &&
                 <span className="red"><ArrowDownOutlined /> {trend}</span>}
            </div>
        </div>
    );
}

export default TrendCard;