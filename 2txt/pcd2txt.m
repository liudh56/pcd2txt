
%输入和输出文件路径及名称
input_pcd = '7_ascii.pcd';
output_txt = 'output.txt';


% 读取PCD文件
fid = fopen(input_pcd, 'r');
if fid == -1
    error('无法打开文件: %s', input_pcd);
end

% 初始化结果数组
result = [];

% 读取文件内容
data_lines = textscan(fid, '%s', 'Delimiter', '\n');
fclose(fid);
data_lines = data_lines{1};

% 解析数据行
for i = 1:length(data_lines)
    line = data_lines{i};
    values = sscanf(line, '%f');
    if length(values) >= 3
        x = values(1);
        y = values(2);
        z = values(3);
        if isfinite(x) && isfinite(y) && isfinite(z)
            result = [result; x, y, z]; %#ok<AGROW>
        else
            fprintf('无效点: %f %f %f\n', x, y, z);
        end
    else
        fprintf('解析失败的行: %s\n', line);
    end
end

% 检查结果是否为空
if isempty(result)
    warning('结果数组为空，未找到有效数据');
end

% 保存结果到TXT文件
writematrix(result, output_txt, 'Delimiter', ' ');