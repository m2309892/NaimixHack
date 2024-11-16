import React, { useCallback } from 'react';
// import { PlusOutlined, FilterOutlined} from '@ant-design/icons';
// import { Input } from "antd";
// import { SvgMenu } from '../../components/Icons';
// import TableGen from './Table';


const InnerUser = ({setPage, page}) => {

    return(
        <>
        <h1 className="h1">Расчитать совместимость</h1>
        {/* <div className="inner">
            <div className="tools">
            <Input 
            suffix={SvgMenu}
            />
            <button onClick={() => {navigate('/add')}}>Рассчитать</button>
            <button onClick={() => {navigate('/compatibility')}}><PlusOutlined /></button>
            <button><FilterOutlined /></button>
          </div>
          <TableGen/>
        </div> */}
        </>
    )
}

export default InnerUser;