import React, {useState} from 'react';
import {  Menu } from 'antd';
import {HomeOutlined, CalendarOutlined, UserOutlined, SettingOutlined} from '@ant-design/icons';


const Navbar = ({setPage, page}) => {
    const [stateOpenKeys, setStateOpenKeys] = useState(['2', '23']);

    
    const items = [
        {
          key: 'sub1',
          icon: <HomeOutlined />,
          label: 'Личный кабинет',
          children: [
            { key: '1', label: 'Общая информация' },
            { key: '2', label: 'Сотрудники' },
            { key: '3', label: 'Команды' },
          ],
        },
        {
          key: '4',
          icon: <CalendarOutlined />,
          label: 'Объявления',
        },
        {
          key: '5',
          label: 'Отклики',
          icon: <UserOutlined />,
        },
        {
          key: '6',
          label: 'Чаты',
          icon: <UserOutlined />,
        },
        {
          key: '7',
          icon: <SettingOutlined />,
          label: 'Настройки',
        },
      ];


    const onOpenChange = (openKeys) => {
        const currentOpenKey = openKeys.find((key) => stateOpenKeys.indexOf(key) === -1);
        // open
        if (currentOpenKey !== undefined) {
          const repeatIndex = openKeys
            .filter((key) => key !== currentOpenKey)
            .findIndex((key) => levelKeys[key] === levelKeys[currentOpenKey]);
    
          setStateOpenKeys(
            openKeys
              // remove repeat key
              .filter((_, index) => index !== repeatIndex)
              // remove current level all child
              .filter((key) => levelKeys[key] <= levelKeys[currentOpenKey]),
          );
        } else {
          // close
          setStateOpenKeys(openKeys);
        }
      };

            
        const getLevelKeys = (items1) => {
            const key = {};
            const func = (items2, level = 1) => {
            items2.forEach((item) => {
                if (item.key) {
                key[item.key] = level;
                }
                if (item.children) {
                func(item.children, level + 1);
                }
            });
            };
            func(items1);
            return key;
        };
        
        const levelKeys = getLevelKeys(items);

    return(
        <>
        <Menu
            style={{ height: '100vw', width: 340 }}
            defaultOpenKeys={['sub1']}
            mode="inline"
            defaultSelectedKeys={['231']}
            openKeys={stateOpenKeys}
            onOpenChange={onOpenChange}
            items={items}
            onClick = {({item, key, keyPath, domEvent}) => {setPage(key);}}
      />
        </>
    )
}


export default Navbar;
