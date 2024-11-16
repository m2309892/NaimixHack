import React, { useCallback, useEffect, useState } from 'react';
import TrendCard from './cardTrend/cardTrend';
// import { PlusOutlined, FilterOutlined} from '@ant-design/icons';
// import { Input } from "antd";
// import { SvgMenu } from '../../components/Icons';
// import TableGen from './Table';


const InnerUser = ({setPage, page}) => {
    const [data, setData] = useState(null);

    useEffect(() => {
        setData({data: 45, trend: 23});

    }, [])

    return(
        <>
        <h1 className="h1">Совместимость</h1>
        <TrendCard  data={data.data} trend={data.trend}/>
        <div className="inner">
        </div>
        </>
    )
}

export default InnerUser;