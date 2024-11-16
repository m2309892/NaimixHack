import React, { useCallback } from 'react';
import { PlusOutlined, FilterOutlined} from '@ant-design/icons';
import { Input } from "antd";
import { SvgMenu } from '../../components/Icons';
import TableGen from './Table';
import { useNavigate } from "react-router-dom";


const InnerResearch = ({setPage, page,  band, setBand}) => {
    const navigate = useNavigate();

    return(
        <>
        <h1 className="h1">Информация про сотрудника</h1>
        <div className="inner">
            <div className="tools">
            <Input 
            
            suffix={SvgMenu}
            />
            <div className="filters">
                <button onClick={() => {navigate('/add')}}><img src="..\..\..\..\public\token.svg"/> Рассчитать</button>
                <button onClick={() => {navigate('/compatibility')}}><PlusOutlined /></button>
                <button><FilterOutlined /></button>
            </div>
          </div>
          <TableGen setBand={setBand} band={band}/>
        </div>
        </>
    )
}

export default InnerResearch;