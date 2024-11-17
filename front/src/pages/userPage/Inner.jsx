import React, { useCallback, useState } from 'react';
import { PlusOutlined, FilterOutlined} from '@ant-design/icons';
import { Input } from "antd";
import { SvgMenu } from '../../components/Icons';
import TableGen from './Table';
import { useNavigate } from "react-router-dom";
import GroupCard from '../../components/groupCard/groupCard'


const InnerResearch = ({setPage, page,  band, setBand}) => {
    const navigate = useNavigate();
    const [open, setOpen] = useState(false);

    return(
        <>
        <h1 className="h1">Информация про сотрудника</h1>
        <div className="inner">
            <div className="tools">
            <Input 
            
            suffix={SvgMenu}
            />
            <div className="filters">
                <button onClick={() => {}}><img src="..\..\..\..\public\token.svg"/> Рассчитать</button>
                <button onClick={() => {navigate('/add')}}><PlusOutlined /></button>
                <button><FilterOutlined /></button>
            </div>
          </div>
          <div className="groups">
            <GroupCard name={'Команда проектировки'} special={'ux/ui design'} key={0} band={band} setBand={setBand}/>
            <GroupCard name={'Команда проектировки'} special={'ux/ui design'} key={0} band={band} setBand={setBand}/>
            <GroupCard name={'Команда проектировки'} special={'ux/ui design'} key={0} band={band} setBand={setBand}/>
          </div>
          <TableGen setBand={setBand} band={band}/>
        </div>
        </>
    )
}

export default InnerResearch;